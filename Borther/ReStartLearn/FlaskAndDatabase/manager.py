
# from FlaskUserModel import User
from flask_script import Manager
from app import *

# import sys
# sys.path.append('Brother/ReStartLearn/FlaskAndDatabase')

from Models import User
import sqlite3


manager = Manager(app)


@manager.command  # python manage.py hello
def hello():
    print('hello world - - ')


@manager.option('-m', '--msg', dest='msg_val', default='world')  # python3 manager.py hello_world -m 'zhang'
def hello_world(msg_val):
    print('hello ' + msg_val)


@manager.command
def init_db():
    sql = 'create table if not exists user (id INT, name TEXT)'  # 创建表
    conn = sqlite3.connect('test.db')
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()


@manager.command
def save():
    user = User(2, 'zhang')
    user.save()


@manager.command
def query_all():
    users = User.query()
    for user in users:
        print(user)


if __name__ == '__main__':
    manager.run()



