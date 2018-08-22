from App.ext import db


class Student(db.Model):

    s_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    s_name = db.Column(db.String(16))