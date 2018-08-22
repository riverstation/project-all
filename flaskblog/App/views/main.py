from flask import Blueprint,render_template,request,current_app,redirect,url_for
from App.models import Posts,User
from App.extensions import cache

main = Blueprint('main',__name__)

@main.route('/')
# @cache.cached(timeout=120,key_prefix='index')
def index():
    return redirect(url_for('main.main_cache',page=1))


@main.route('/show/<int:page>/')
# @cache.memoize(timeout=120) #根据不同参数进行数据的缓存
def main_cache(page):
    print('你能看到我几次。。。')
    # try:
    #     page = int(request.args.get('page', 1))
    # except:
    #     page = 1
    p = Posts.query.filter_by(pid=0).order_by(Posts.timestamp.desc()).paginate(page, current_app.config['CON_NUM'],False)
    data = p.items  # 当前页的数据
    return render_template('main/index.html', data=data, pagination=p)



@main.route('/test/')
def test():
    u1 = User.query.get(1)
    p1 = Posts.query.get(3)
    #1号用户 收藏 1号帖子
    # u1.favorites.append(p1)
    # print(u1.favorites.all())
    # print(p1.users.all())
    u1.favorites.remove(p1)
    return 'test'