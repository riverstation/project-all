from App.extensions import db
from werkzeug.security import generate_password_hash,check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Seralize
from flask import current_app #current_app app对象的代理对象 获取真正的app对象或者app对象的配置 config
from flask_login import UserMixin
from App.extensions import login_manager

class User(UserMixin,db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(13),unique=True)
    password_hash = db.Column(db.String(128))
    age = db.Column(db.Integer,default=18)
    sex = db.Column(db.Boolean,default=True)
    email = db.Column(db.String(50))
    icon = db.Column(db.String(37),default='default.jpg')
    confirm = db.Column(db.Boolean,default=False) #当前用户激活状态 默认未激活
    """
    db.relationship 建立模型关系 在表中不存在 提供的模型之间的操作
    Posts  和哪个模型建立关系
    backref 反向引用字段名称 给添加关系的模型 添加一个属性 user
    lazy 加载时机  对象的方式
    """
    posts = db.relationship('Posts',backref='user',lazy='dynamic')

    #添加关系的模型
    #多对多中 指定读取数据的中间表的名称
    favorites = db.relationship('Posts',secondary='collections',backref=db.backref('users',lazy='dynamic'),lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('属性不存在')
    @password.setter
    def password(self, password):
        #将密码在内部加密 在传递
        self.password_hash = generate_password_hash(password)

    #生成token的方法 执行这个函数之前必须数据已经插入到数据库 并获取id值
    def generate_token(self):
        s = Seralize(current_app.config['SECRET_KEY'])
        return s.dumps({'id':self.id})

    #用户激活
    @staticmethod
    def check_token(token):
        try:
            #生成token对象
            s = Seralize(current_app.config['SECRET_KEY'])
            Dict = s.loads(token) #加载出字典
            uid = Dict['id'] #获取用访问的id
            # 获取 访问过来人的对象
            u = User.query.get(uid)
            if not u:
                raise ValueError
        except:
            return False
        #判断是否没有激活 没有激活 则激活  否则返回真
        if not u.confirm:
            u.confirm = True
            db.session.add(u)

        return True




    #验证密码
    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

#登录认证的回调函数  如果该回调函数 不存在 则报错
@login_manager.user_loader
def user_loader(uid):
    return User.query.get(int(uid))
