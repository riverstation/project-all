from flask import Flask

from App.apis import init_api
from App.ext import init_ext
from App.settings import envs


def create_app(env):

    app = Flask(__name__)
    # 初始化 app的配置
    app.config.from_object(envs.get(env))

    # 初始化扩展库
    init_ext(app=app)

    init_api(app)

    return app