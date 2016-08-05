import pymongo
from pymongo import MongoClient
client = MongoClient('localhost', 27017)

db = client.zhang
zhangT = db.user
#
zhangT.insert_one({"name": "handabaobao", "email": "129#1444", "nimei": "33"})
zhangT.insert_one({"name": "handabaobao", "email": "125#1444", "nimei": "33"})
zhangT.insert_one({"name": "handabaobao", "email": "126#1444", "nimei": "33"})
zhangT.insert_one({"name": "handabaobao", "email": "127#1444", "nimei": "33"})
zhangT.insert_one({"name": "handabaobao", "email": "12d#1444", "nimei": "33"})
#

# zhangT.insert_one({"mmm": 10})

# zhangT.find_one()
# for item in zhangT.find({"name":"handabaobao"}):
#     print(item)

for item in zhangT.find({"name": "handabaobao"}).sort("email", pymongo.ASCENDING):
    print(item['email'])

