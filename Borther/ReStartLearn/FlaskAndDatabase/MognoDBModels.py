
from ReStartLearn.FlaskAndDatabase.MognoDBApp import db


class User(db.Document):
    name = db.StringField()
    email = db.StringField()

    def __str__(self):
        return 'name:{}--email:{}'.format(self.name,self.email)






