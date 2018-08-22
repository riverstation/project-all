from flask import Flask,render_template,render_template_string
from flask_script import Manager
from flask_mail import Mail,Message
import os

app = Flask(__name__)
app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER','smtp.1000phone.com')
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME','xialigang@1000phone.com')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD','123456')
mail = Mail(app)
manager = Manager(app)


@app.route('/send_mail/')
def send_mail():
    msg = Message(subject='邮件激活',recipients=['793390457@qq.com'],sender=app.config['MAIL_USERNAME'])

    msg.html = render_template_string('<h1>你好 请点击右侧链接 进行账户的激活 <a href="http://www.baidu.com">激活</a></h1>')

    mail.send(message=msg) #发送邮件
    return render_template_string('发送邮件')



if __name__ == '__main__':
    manager.run()


"""
windows  set 名=值
set 名

linux
export 名=值
echo $名
"""