#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from flask import Flask, render_template, flash, request, abort

app = Flask(__name__)
# app.sercet_key = '123'  #   #妈的 在这里设置不起作用??? 幸好打开了 debug=True .

# @app.route('/')  # 直接写在代码里面
# def hello_world():
#     flash('hello zhangxianqiang')
#     return render_template('exception.html')


@app.route('/')
def hello_world():
    flash("hello 张宪强")
    return render_template("login.html")


@app.route('/login', methods=['POST'])
def login():
    form = request.form
    username = form.get('username')
    password = form.get('password')

    if not username:
        flash('please input username')
        return render_template('login.html')
    if not password:
        flash('please input password')
        return render_template('login.html')

    if username == 'zhangxianqiang' and password == '123456':
        flash('login success')
        return render_template('login.html')
    else:
        flash('username or password wrong')
        return render_template('login.html')


@app.errorhandler(404)
def error404(e):
    return render_template('404.html')

@app.route('/users/<user_id>')
def user(user_id):
    if int(user_id) == 1:
        return render_template('user.html')
    else:
        abort(404)

if __name__ == '__main__':
    app.secret_key = 'super secret key'  # 使用这个key flask 会对消息进行加密
    # app.config['SESSION_TYPE'] = 'filesystem'
    # sess.init_app(app)
    app.run(port=5003, debug=True)


