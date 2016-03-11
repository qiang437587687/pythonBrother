#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from flask import Flask, render_template, flash

app = Flask(__name__)
# app.sercet_key = '123'  #   #妈的 在这里设置不起作用??? 幸好打开了 debug=True .

# @app.route('/')  # 直接写在代码里面
# def hello_world():
#     flash('hello zhangxianqiang')
#     return render_template('exception.html')


@app.route('/')
def hello_world():
    flash("hello 张宪强")
    return render_template("exception.html")


if __name__ == '__main__':
    app.secret_key = 'super secret key'  # 使用这个key flask 会对消息进行加密
    # app.config['SESSION_TYPE'] = 'filesystem'
    # sess.init_app(app)
    app.run(port=5003, debug=True)


