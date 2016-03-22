from app import app
from flask import render_template, request
from app.models import Todo, TodoForm
from datetime import datetime


@app.route('/')
def index():
    form = TodoForm()
    # todos = Todo.objects.all()
    todos = Todo.objects.order_by('-time')
    return render_template('index.html', todos=todos, form=form)


@app.route('/add', methods=['POST'])
def add():

    form = TodoForm(request.form)
    if form.validate():
        content = form.content.data
        todo = Todo(content=content, time=datetime.now())
        todo.save()
    # todos = Todo.objects.all()
    todos = Todo.objects.order_by('-time')

    return render_template('index.html', todos=todos, form=form)

    # form = request.form  # 用上面的 form 直接实例化form  用wtf 来验证表单数据
    # content = form['content']
    # todo = Todo(content)   # 能进行存储的Todo model
    # todo.save()   # 这个不是自己写的 应该是 mongoengine 里面已经提供好了
    # todos = Todo.objects.all()
    # return render_template('index.html', todos=todos)


@app.route('/done/<string:todo_id>')
def done(todo_id):
    form = TodoForm()
    todo = Todo.objects.get_or_404(id=todo_id)
    todo.status = 1
    todo.save()
    # todos = Todo.objects.all()
    todos = Todo.objects.order_by('-time')

    return render_template('index.html', todos=todos, form=form)


@app.route('/undone/<string:todo_id>')
def undone(todo_id):
    form = TodoForm()
    todo = Todo.objects.get_or_404(id=todo_id)
    todo.status = 0
    todo.save()
    # todos = Todo.objects.all()
    todos = Todo.objects.order_by('-time')

    return render_template('index.html', todos=todos, form=form)


@app.route('/delete/<string:todo_id>')
def delete(todo_id):
    form = TodoForm()
    todo = Todo.objects.get_or_404(id=todo_id)
    todo.delete()
    # todos = Todo.objects.all()
    todos = Todo.objects.order_by('-time')

    return render_template('index.html', todos=todos, form=form)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')

