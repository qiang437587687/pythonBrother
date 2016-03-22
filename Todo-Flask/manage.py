
from app import app
from app.models import Todo
from flask.ext.script import Manager


manager = Manager(app)


@manager.command
def save():
    todo = Todo(content="study mistake")
    todo.save()


# save()      # 直接调用测试了 暂时测试时候先不用这个了

if __name__ == '__main__':
    manager.run()

# from app import app
# from app.models import Todo
# from flask.ext.script import Manager
# #
# #
# manager = Manager(app)
# #
# @manager.command
# def save():
#     todo = Todo(content="study flask")
#     todo.save()
# #
# #
# if __name__ == '__main__':
#     manager.run()
# #