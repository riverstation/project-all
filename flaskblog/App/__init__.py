from flask import Flask
from .settings import config #配置文件的字典
from .extensions import extensions_init #加载第三方扩展库函数
from .views import blueprint_register #蓝本注册函数

# 创建app并初始化所有包文件的函数
def create_app(configName):
    app = Flask(__name__)
    #加载配置文件
    app.config.from_object(config[configName])
    #初始化所有第三方扩展库的函数
    extensions_init(app)
    # 蓝本注册函数
    blueprint_register(app)
    return app

