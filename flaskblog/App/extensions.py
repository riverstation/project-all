from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate #导入迁移类
from flask_mail import Mail
from flask_login import LoginManager #处理登录的模块
from flask_uploads import UploadSet,configure_uploads,patch_request_class,IMAGES
from flask_moment import Moment #格式化时间 和显示时间差值的模块
from flask_cache import Cache


bootstrap = Bootstrap()
db = SQLAlchemy()
migrate = Migrate(db=db) #实例化迁移文件类
mail = Mail()
login_manager = LoginManager()
file = UploadSet('photos',IMAGES)
moment = Moment()
# cache = Cache(config={"CACHE_TYPE":'simple'})#实例化缓存 简单的缓存
cache = Cache(config={"CACHE_TYPE":'redis'})#实例化缓存 简单的缓存

#所有第三方扩展库初始化的函数
def extensions_init(app):
    moment.init_app(app)
    bootstrap.init_app(app)
    db.init_app(app)
    migrate.init_app(app=app)
    mail.init_app(app)
    cache.init_app(app=app) #缓存

    login_manager.init_app(app)
    #指定登录的端点
    login_manager.login_view = 'user.login'
    login_manager.login_message = '您还没有登录 请登录后在访问'
    #设置session不同等级的安全 设置为strong FLask——login会记录客户端IP地址 和浏览器代理信息  如果发生任何的异常 则退出登录
    #None basic strong
    login_manager.session_protection = 'strong'
    #配置文件上传
    configure_uploads(app,file)
    patch_request_class(app,size=None)

"""
python3 manage.py db init
python3 manage.py db migrate
python3 manage.py db upgrade
"""