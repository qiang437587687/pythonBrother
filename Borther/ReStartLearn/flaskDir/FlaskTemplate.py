#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  ps -fA | grep python  查看占用的端口的python进程

from flask import Flask, render_template

from ReStartLearn.flaskDir.Models import User  # 这里面一直提示是有error的.

app = Flask(__name__)

# @app.route('/')  # 直接写在代码里面
# def hello_world():
#     return '<h1>Hello World</h1>'


# @app.route('/')  # 传入的是idnex.html文件
# def hello_world():
#     return render_template('index.html')

@app.route('/')  # 传入html里面进行加载
def hello_world():
    return render_template('index.html', content='hello zhang')


@app.route('/user')
def user_index():
    user = User(1, 'zhangxianqiang')
    return render_template('user_index.html', user=user)


@app.route('/query_user/<user_id>')  # 前面的 / 别忘记加了 要不会有错误 urls must start with a leading slash
def query_user(user_id):
    user = None
    if int(user_id) == 1:
        user = User(1, 'zhangxianqiang')
    return render_template('user_id.html', user=user)


@app.route('/users')
def user_list():
    users = []
    for i in range(1, 11):
        user = User(i, 'zhangxianqiang' + str(i))
        users.append(user)
    return render_template('user_list.html', users=users)


# 下面这两个测试一下 模板的继承


@app.route('/one')
def return_one():
    return render_template('one_base.html')


@app.route('/two')
def return_two():
    return render_template('two_base.html')

if __name__ == '__main__':
    app.run(port=5003)

