from pymysql_comm import UsingMysql
import datetime

# 新增单条记录
def create_one(data):
    with UsingMysql(log_time=True) as um:
        try:
            sql = "insert into chatgpt.chatgpt_question_answer(twitter_id,full_text,lang,favorite_count,retweet_count,time,hashtags) " + \
                  "values(%s,%s,%s,%s,%s,%s,%s)"
            hashtags = data['entities']['hashtags']
            strhashtag = ''
            for hashtag in hashtags:
                strhashtag = strhashtag + ',' + hashtag['text']
            params = (data['id'], data['full_text'], data['lang'], data['favorite_count'], data['retweet_count'])
            um.cursor.execute(sql, params)
        except BaseException as e:
            print(e)


def select_by_id(id):
    with UsingMysql(log_time=True) as um:
        sql = 'select * from chatgpt.chatgpt_question_answer where id = %s'
        params = (id)
        um.cursor.execute(sql, params)
        return um.cursor.fetchone()

def selectAll():
    with UsingMysql(log_time=True) as um:
        sql = "select * from chatgpt.chatgpt_question_answer where is_valid=1 and ai_ppl = 0"
        um.cursor.execute(sql)
        return um.cursor.fetchall()

def exit(id):
    with UsingMysql(log_time=True) as um:
        sql = 'select * from chatgpt.chatgpt_question_answer where twitter_id = %s'
        params = (id)
        um.cursor.execute(sql, params)
        data = um.cursor.fetchone()
        if data is None:
            return False
        else:
            return True

def update(id, ai_reply):
    with UsingMysql(log_time=True) as um:
        try:
            sql = 'update chatgpt.chatgpt_question_answer set ai_reply=%s where id = %s'
            params = (ai_reply, id)
            um.cursor.execute(sql, params)
        except BaseException as e:
            print(e)

def updateppl(id, human_ppl, ai_ppl):
    with UsingMysql(log_time=True) as um:
        try:
            sql = 'update chatgpt.chatgpt_question_answer set human_ppl=%s, ai_ppl=%s where id = %s'
            params = (human_ppl, ai_ppl, id)
            um.cursor.execute(sql, params)
        except BaseException as e:
            print(e)