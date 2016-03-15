import sqlite3


def get_conn():
    return sqlite3.connect('test.db')


class User(object):
    def __init__(self, id, name):
        self.name = name
        self.id = id

    def save(self):
        sql = 'insert into user VALUES (?, ?)'
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(sql, (self.id, self.name))
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod  # 静态方法
    def query():
        sql = 'select * from USER'
        conn = get_conn()
        cursor = conn.cursor()
        rows = cursor.execute(sql)
        users = []
        for row in rows:
            user = User(row[0], row[1])
            users.append(user)
        conn.commit()
        cursor.close()
        conn.close()
        return users

    def __str__(self):
        return 'id:{}--name:{}'.format(self.id, self.name)


