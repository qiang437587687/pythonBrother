#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
from flask import url_for
app = Flask(__name__)


@app.route('/')  # 最简单的路由
def hello_world():
    return 'hello world'


@app.route('/zhang', methods=['POST', 'GET'])  # 这个地方的方法要放到 [] 里面 现在是两个都可以.!
def hello_zhang():
    return 'hello zhang'


@app.route('/users/<id>')  # url 里面获取 数据 id
def user_id(id):
    return 'hello user:' + id


@app.route('/query_user')  # 访问要是这样的   http://127.0.0.1:5001/query_user?id=1234
def query_user():
    id = request.args.get('id')
    return 'hello user:' + id

@app.route('/query_url') # flask 的反向路由
def query_url():
    return 'query_url' + url_for('query_user')


if __name__ == '__main__':
    app.run(port=5001)


# from flask import Flask, request, url_for
# app = Flask(__name__)
#
#
# @app.route('/')
# def hello_world():
#     return 'Hello World!'
#
# if __name__ == '__main__':
#     app.run()
