from time import sleep

from flask import Blueprint, render_template

from App.ext import cache

user = Blueprint("user", __name__)


@user.route("/")
@cache.cached(timeout=10)
def index():

    sleep(5)

    return "User Index"


@user.route("/cache/")
def have_cache():

    result = cache.get("have_cache")

    if result:
        return result

    resp = render_template('HaveCache.html')

    sleep(2)

    cache.set("have_cache", resp, timeout=10)

    return resp