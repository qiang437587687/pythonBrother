import pymongo

def get_coll():

    client = pymongo.MongoClient('localhost', 27017)
    db = client.zhang
    user = db.user_colletion

    return user


class User(object):

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def save(self):
        user = {'name': self.name, 'email': self.email}
        coll = get_coll()
        id = coll.insert(user)
        print(id)

    @staticmethod
    def query_user():
        users = get_coll().find()
        return users



