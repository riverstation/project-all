from App.extensions import db
from datetime import datetime

class Posts(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer,primary_key=True)
    content = db.Column(db.Text)
    pid = db.Column(db.Integer,default=0)
    path = db.Column(db.String(255),default='0,')
    #记录时间的
    timestamp = db.Column(db.DateTime,default=datetime.utcnow)
    #user的外键
    uid = db.Column(db.Integer,db.ForeignKey('user.id'))