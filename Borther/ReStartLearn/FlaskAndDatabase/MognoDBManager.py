from flask_script import Manager
from MognoDBApp import app
from MognoDBFlask import User

manager = Manager(app)

@manager.command
def save():
    user = User('zhang', '124@163.com')
    user.save()


@manager.command
def query_users():
    users = User.query_user()
    for user in users:
        print(user)

save()
query_users()


if __name__ == '__main__':
    manager.run()

