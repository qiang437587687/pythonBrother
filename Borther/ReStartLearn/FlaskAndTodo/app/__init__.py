
from flask import Flask

from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)

app.config.from_object('config') # 实例化配置

db = MongoEngine(app)  # 实例化mongoEngine

from ReStartLearn.FlaskAndTodo.app import views, models

