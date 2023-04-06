import openai
import chatgpt_sql
import threading
openai.api_key = "**************"
all_chat = chatgpt_sql.selectAll()
ids = []
for row in all_chat:
    ids.append(row['id'])
index = 0

def askChatGPT(id):
    row = chatgpt_sql.select_by_id(id)[0]
    prompt = row['title']
    model_engine = "text-davinci-003"
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completions.choices[0].text
    print("Q:"+prompt)
    print("A:"+message.strip())
    chatgpt_sql.update(row['id'], message.strip())

class My_Thread(threading.Thread):
    def __init__(self, lock, name):
        super().__init__()
        self.lock = lock
        self.name = name

    def run(self):
        while True:
            self.lock.acquire()
            print(self.name, '获取锁，并进入共享区域f()')
            global index
            global ids
            index = index + 1
            self.lock.release()
            print(self.name, '退出共享区域f()，并释放锁')
            askChatGPT(ids[index])

lock = threading.Lock()
t1 = My_Thread(lock, "Thread 1")
t2 = My_Thread(lock, "Thread 2")

t1.start()
t2.start()

print('主线程结束')