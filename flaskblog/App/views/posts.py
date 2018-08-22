from flask import Blueprint,render_template,flash,redirect,url_for,jsonify
from App.forms import Posts as FormPosts
from App.models import Posts
from flask_login import current_user
from App.extensions import db

posts = Blueprint('posts',__name__)



#发表帖子
@posts.route('/send_posts/',methods=['GET','POST'])
def send_posts():
    form = FormPosts()
    if form.validate_on_submit():
        if current_user.is_authenticated:
            u = current_user._get_current_object() #拿到真正的当前用户对象 u
            p = Posts(content=form.content.data,user=u)
            db.session.add(p)
            flash('发表成功！！ 请前往首页查看')
            return redirect(url_for('posts.send_posts'))
        else:
            flash('您还没有登录 请前去登录')
            return redirect(url_for('user.login'))
    return render_template('posts/send_posts.html',form=form)


#给与取消收藏的接口
@posts.route('/favorite/<int:pid>/')
def favorite(pid):
    return jsonify({'code':200})