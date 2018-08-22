from App.ext import db


class Movie(db.Model):

    m_id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    m_name = db.Column(db.String(16))

    def to_dict(self):
        return {"m_id": self.m_id, "m_name": self.m_name}