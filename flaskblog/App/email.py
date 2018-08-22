from flask import Flask,render_template,current_app
from flask_mail import Message
from threading import Thread #导入线程
from .extensions import mail


def async_send_mail(app,msg):
    #开启程序上下文
    with app.app_context():
        mail.send(message=msg) #发送邮件

def send_mail(subject,to,tem,**kwargs):
    """
    :param subject: 邮件主题
    :param to: 接收邮件的人
    :param tem: 邮件的模板
    :param kwargs: 给模板中传递的参数（变量）
    :return: None
    """
    app = current_app._get_current_object() #拿到实例化的app对象
    msg = Message(subject=subject,recipients=[to],sender=app.config['MAIL_USERNAME'])
    msg.html = render_template('email/'+tem+'.html',**kwargs)
    thr = Thread(target=async_send_mail,args=(app,msg))
    thr.start() #开启线程



