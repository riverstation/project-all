from flask import Blueprint,render_template,flash,redirect,url_for,request,current_app
from App.forms import Register,AccountActivate,Login,Icon #导入wtf注册类
from App.models import User #导入user模型类
from App.extensions import db,file
from App.email import send_mail #导入发送邮件的函数
from flask_login import login_required,login_user,logout_user,current_user
from PIL import Image
import os

user = Blueprint('user',__name__)

#注册
"""
1. 模型类
2. 实例化 传入数据
3. 生成token
4. 发送邮件
5. 激活注册账户
6. 注册完成
"""
@user.route('/register/',methods=['GET','POST'])
def register():
    form = Register()
    if form.validate_on_submit():
        u = User(username=form.username.data,password=form.userpass.data,email=form.email.data)
        db.session.add(u)
        db.session.commit()
        token = u.generate_token()
        # return token
        send_mail('邮件激活',form.email.data,'activate',username=form.username.data,token=token,urlFor='user.activate')
        flash('注册成功 请注意查收')
        return redirect(url_for('user.login')) #注册成功 跳转到登录
    return render_template('user/register.html',form=form)



#用户的激活
@user.route('/activate/<token>/')
def activate(token):
    if User.check_token(token):
        flash('激活成功 请去登录')
        return redirect(url_for('user.login'))

    else:
        flash('激活失败 请重新激活')
        return redirect(url_for('user.register'))


#注册以后 激活链接失效 重新激活
@user.route('/accountactivation/',methods=['GET','POST'])
def accountactivation():
    form = AccountActivate()
    if form.validate_on_submit():
        #查询用户输入的数据是否存在
        u = User.query.filter_by(username=form.username.data,email=form.email.data).first()
        if not u: #用户不存在
            flash('您输入的信息有误 请重新输入')
        elif u.confirm: #用户已激活
            flash('该账户已经激活 请去登录')
        #检测密码
        elif not u.check_password(form.userpass.data):
            flash('您输入的密码有误')
        #生成token 发送邮件
        else:
            token = u.generate_token()
            send_mail('邮件激活',form.email.data, 'activate', username=form.username.data, token=token,
                      urlFor='user.activate')
            flash('邮件发送成功 请注意查收')
            return redirect(url_for('user.login'))
    return render_template('user/accountactivate.html',form=form)


#登录
# http://www.pythondoc.com/flask-login/
@user.route('/login/',methods=['GET','POST'])
def login():
    form = Login()
    if form.validate_on_submit():
        u = User.query.filter_by(username=form.username.data).first()
        if not u:
            flash('当前用户不存在')
        elif not u.confirm:
            flash('当前用户未激活')
        elif not u.check_password(form.userpass.data):
            flash('请输入正确的密码')
        else:
            # pass #处理登录 状态保持
            login_user(u)
            flash('登录成功')
            return redirect(request.args.get('next',url_for('main.index')))
    return render_template('user/login.html',form=form)


#退出登录
@user.route('/logout/')
def logout():
    logout_user()
    flash('退出登录成功')
    return redirect(url_for('main.index'))

#这是一个必须登录才能访问的路由地址
@user.route('/test/')
@login_required
def test():
    # 如果没登录访问了 必须登录才能访问的地址 则登录以后 回到上一次访问的位置
    return 'test'

#随机图片名称的函数
def random_filename(suffix,length=32):
    import random,string
    Str = string.ascii_letters+'0123456789'
    return ''.join(random.choice(Str) for i in range(length))+'.'+suffix


#图片缩放
def img_zoom(path,prefix='s_',width=100,height=100):
    img = Image.open(path)
    img.thumbnail((width,height))
    pathTuple = os.path.split(path) #拆分图片和路径
    newPath = os.path.join(pathTuple[0],prefix+pathTuple[1]) #重新拼凑新路径
    img.save(newPath) #保存新路经




#修改头像
@user.route('/change_icon/',methods=['GET','POST'])
def change_icon():
    form = Icon()
    if form.validate_on_submit():
        filename = form.icon.data.filename
        suffix = filename.split('.')[-1]
        #循环确保生成的图片名称唯一性
        while True:
            filename = random_filename(suffix)
            path = os.path.join(current_app.config['UPLOADED_PHOTOS_DEST'],filename)
            if not os.path.exists(path):
                break
        file.save(form.icon.data,name=filename) #保存图片
        #删除之前的图片
        #原图一张
        #在首页展示的时候 一张 大小为100  s_
        if current_user.icon != 'default.jpg':
            os.remove(os.path.join(current_app.config['UPLOADED_PHOTOS_DEST'],current_user.icon))
            os.remove(os.path.join(current_app.config['UPLOADED_PHOTOS_DEST'],'s_'+current_user.icon))
        #执行缩放
        img_zoom(path)

        current_user.icon = filename
        #数据保存到表中
        db.session.add(current_user)
        #获取图片地址
    img_url = file.url(current_user.icon)
    return render_template('user/icon.html',form=form,img_url=img_url)