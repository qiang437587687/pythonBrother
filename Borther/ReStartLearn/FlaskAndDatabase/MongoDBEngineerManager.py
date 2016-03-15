from flask_script import Manager
from MognoDBApp import app
from MognoDBModels import User

manager = Manager(app)

@manager.command
def save():
    # user = User('zhang', '124@163.com')
    # user.save()

    user = User(name='handabao', email='123@163.com')
    user.save()


@manager.command
def query_users():
    # users = User.query_user()
    # for user in users:
    #     print(user)

    users = User.objects.all()
    for user in users:
        print(user)


save() # 调用~~~
query_users()


if __name__ == '__main__':
    manager.run()