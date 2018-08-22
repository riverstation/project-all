import os
base_dir = os.path.abspath(os.path.dirname(__file__))
class Config:
    #密钥
    SECRET_KEY = 'abcdef'
    #加载本地bootdtrp
    BOOTSTRAP_SERVE_LOCAL = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True #自动提交
    #配置发送邮件
    MAIL_SERVER = os.environ.get('MAIL_SERVER','smtp.1000phone.com')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME','xialigang@1000phone.com')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD','123456')

    #配置上传文件大小
    MAX_CONTENT_LENGTH = 1024*1024*64
    UPLOADED_PHOTOS_DEST = os.path.join(base_dir,'static/upload')

    #配置每页显示数据的条数
    CON_NUM = 5

#配置不同开发环境的数据库和配置

#配置开发的配置
class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/dev_blog'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(base_dir,'dev-blog.sqlite')
    DEBUG = True


#配置测试环境
class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/test_blog'
    DEBUG = False

#配置生产环境
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/blog'
    DEBUG = False

config = {
    'production':ProductionConfig,
    'testing':TestingConfig,
    'development':DevelopmentConfig,
    #默认开发环境
    'default':DevelopmentConfig
}




