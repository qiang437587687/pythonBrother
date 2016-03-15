from flask import Flask

from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {'db': 'zhang'}


db = MongoEngine(app)



@app.route('/')
def hello_world():
    return 'hello world'

if __name__ == '__main__':
    app.run()
