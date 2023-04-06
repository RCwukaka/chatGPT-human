import chatgpt_sql
import nltk

def Normalize_corpus(df):
    corpus_norm = []
    for doc in df.full_text:
        if len(doc) < 100:
            continue
        # 进行分词操作
        con = []
        tokens = nltk.word_tokenize(doc)
        pos_tags = nltk.pos_tag(tokens)
        for word, pos in pos_tags:
            con.append(word)
        corpus_norm.append(con)
    return corpus_norm

# from snownlp import SnowNLP
# all_chat = chatgpt_sql.selectAll()
# for row in all_chat:
#     human = SnowNLP(row['reply'])
#     ai = SnowNLP(row['ai_reply'])
#     print(row['id'])
#     chatgpt_sql.updateSentiment(row['id'], human.sentiments, ai.sentiments)

import jieba.posseg as posseg
import chatgpt_qa_sql
from enum import Enum
text = "不会啊，办理广发银行信用卡很简单的"
# jieba.cut直接得到generator形式的分词结果
all_chat = chatgpt_sql.selectAll()
data = {
    "word":"",
    "corpus":"",
    "type":"",
    "qa_id":0
}
class corpus(Enum):
    a = 'adj'
    b = 'noun'
    c = 'conj'
    d = 'adv'
    e = 'modal particle'
    f = 'adv'
    i = 'idiom'
    j = 'acronym'
    m = 'num'
    n = 'noun'
    p = 'prep'
    r = 'pron'
    s = 'acronym'
    t = 'adv'
    u = 'aux'
    v = 'verb'
    x = 'punc'
    z = 'modal particle'

print(corpus['a'].value)

for row in all_chat:
    seg = posseg.cut(row['reply'])
    for se in seg:
        data['word'] = se.word
        data['corpus'] = corpus[se.flag[0:1]].value
        data['type'] = 1
        data['qa_id'] = row['id']
        chatgpt_qa_sql.create_one(data)
    seg = posseg.cut(row['ai_reply'])
    for se in seg:
        data['word'] = se.word
        data['corpus'] = corpus[se.flag[0:1]].value
        data['type'] = 2
        data['qa_id'] = row['id']
        chatgpt_qa_sql.create_one(data)