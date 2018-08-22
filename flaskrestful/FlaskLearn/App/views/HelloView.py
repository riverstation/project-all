import time

from flask import Blueprint, render_template, request, session

# from App.ext import cache

from App.models.StudentModel import Student

hello = Blueprint("hello", __name__)


@hello.route("/")
def index():
    print("index")

    session["name"] = "江疏影"

    return render_template("hello.html")


@hello.route("/students/")
def students():

    student_list = Student.query.all()

    student_obj = Student()

    student_obj.s_name = "小明666"

    student_obj.s_id = 1000000

    student_list.append(student_obj)

    print(session.get("name"))

    return render_template("student_list.html", student_list=student_list)


@hello.route("/student/")
def student():

    s_id = request.args.get("id")

    return s_id + "的详情"


@hello.route("/search/")
def search():
    content = request.args.get("keyword", "Python")

    return "您搜索的%s存在9000条" % content


@hello.before_request
def before():
    print("before", request.remote_addr)

    # if request.path == "/search/":
    #
    #     ip = request.remote_addr
    #
    #     result = cache.get(ip)
    #
    #     if result:
    #         return "十秒之内只能搜索一次，稍后再来"
    #     else:
    #         cache.set(ip, "666", timeout=10)

    # 两秒之内只能访问一次
    # ip = request.remote_addr
    #
    # result = cache.get(ip)
    #
    # if result:
    #     return '您的访问频率过高'
    # else:
    #     cache.set(ip, "111", timeout=2)

    # 一分钟之内 只能访问20次
    # ip = request.remote_addr
    #
    # black = cache.get("black")
    #
    # if black:
    #     if ip in black:
    #         return "洗洗睡吧，一首凉凉送给你"
    # else:
    #     black = []
    #
    # requests_time = cache.get(ip)
    #
    # if not requests_time:
    #     requests_time = []
    #     # requests_time.append(time.time())
    #     requests_time.insert(0, time.time())
    #     cache.set(ip, requests_time, timeout=60)
    # else:
    #     # 清洗数据， 超过一分钟的数据
    #     while requests_time and time.time() - requests_time[-1] > 60:
    #         requests_time.pop()
    #
    #     requests_time.insert(0, time.time())
    #     cache.set(ip, requests_time, timeout=60)
    #
    #     if len(requests_time) > 35:
    #         black.append(ip)
    #         cache.set("black", black, timeout=60 * 60 * 24)
    #
    #     elif len(requests_time) >= 20:
    #         return "小爬虫回家睡觉把"
    #
    # ip = request.remote_addr
    #
    # blacklist = cache.get("blacklist")
    #
    # if blacklist:
    #     if ip in blacklist:
    #         return "凉凉，洗洗睡吧"
    # else:
    #     blacklist = []
    #
    # if request.path == "/student/":
    #     id = request.args.get("id")
    #     if id == "1000000":
    #         blacklist.append(ip)
    #         cache.set("blacklist", blacklist, timeout=60*60*24*7)
    #         return "什么鬼"


