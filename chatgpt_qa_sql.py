from pymysql_comm import UsingMysql
import datetime

# 新增单条记录
def create_one(data):
    with UsingMysql(log_time=True) as um:
        try:
            sql = "insert into chatgpt.chatgpt_qa_corpus(word,corpus,type,qa_id) " + \
                  "values(%s,%s,%s,%s)"
            params = (data['word'], data['corpus'], data['type'], data['qa_id'])
            um.cursor.execute(sql, params)
        except BaseException as e:
            print(e)


def select_by_id(id):
    with UsingMysql(log_time=True) as um:
        sql = 'select * from chatgpt.chatgpt_qa_corpus where id = %s'
        params = (id)
        um.cursor.execute(sql, params)
        return um.cursor.fetchone()

def selectAll():
    with UsingMysql(log_time=True) as um:
        sql = "select * from chatgpt.chatgpt_qa_corpus"
        um.cursor.execute(sql)
        return um.cursor.fetchall()

def exit(id):
    with UsingMysql(log_time=True) as um:
        sql = 'select * from chatgpt.chatgpt_qa_corpus where id = %s'
        params = (id)
        um.cursor.execute(sql, params)
        data = um.cursor.fetchone()
        if data is None:
            return False
        else:
            return True