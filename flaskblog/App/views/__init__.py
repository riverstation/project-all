from .main import main
from .user import user
from .posts import posts

#配置蓝本注册
defalut_blueprint = [
    (main,''),
    (user,''),
    (posts,''),
]

#注册蓝本
def blueprint_register(app):
    #循环注册蓝本
    for blueprint,url_prefix in defalut_blueprint:
        app.register_blueprint(blueprint,url_prefix=url_prefix)
    # app.register_blueprint('user')