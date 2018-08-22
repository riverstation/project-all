import hashlib

from werkzeug.security import generate_password_hash, check_password_hash

from App.ext import db
from App.models.ModelUtil import BaseModel

# 读
READ = 1
# 赞
PRAISE = 2
# 写
WRITE = 4


class User(BaseModel, db.Model):
    u_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    u_name = db.Column(db.String(16), unique=True)
    _u_password = db.Column(db.String(256))
    is_delete = db.Column(db.Boolean, default=False)
    u_permission = db.Column(db.Integer, default=0)

    @property
    def u_password(self):
        return self._u_password

    @u_password.setter
    def u_password(self, password):
        self._u_password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self._u_password, password)

    def check_permission(self, permission):
        return self.u_permission & permission == permission

    # def set_password(self, password):
    #     password = self._to_hash(password)
    #
    #     self.u_password = password
    #
    # def verify_password(self, password):
    #     # password = self._to_hash(password)
    #     # return self.u_password == password
    #     return check_password_hash(self.u_password, password)
    #
    # def _to_hash(self, password):
    #
    #     # md5 = hashlib.sha512()
    #     # md5.update(password.encode("utf-8"))
    #     # return md5.hexdigest()
    #     return generate_password_hash(password)

