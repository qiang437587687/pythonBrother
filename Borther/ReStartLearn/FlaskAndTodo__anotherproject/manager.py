from ReStartLearn.FlaskAndTodo.app import app
from ReStartLearn.FlaskAndTodo.app.models import Todo
from flask.ext.script import Manager


manager = Manager(app)

@manager.command
def save():
    todo = Todo(content='study flask')
    todo.save()


save() # 这个是直接调用  视频中是 用的终端~

if __name__ == '__main__':
    manager.run()



