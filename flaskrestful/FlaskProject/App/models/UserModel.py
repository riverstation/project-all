from App.ext import db


class User(db.Model):
    u_id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    u_name = db.Column(db.String(16))

