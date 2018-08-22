from flask import Blueprint, request, jsonify

from App.ext import db
from App.models import Movie

movie = Blueprint("movie", __name__)


@movie.route("/movies/", methods=["GET", "POST"])
@movie.route("/movies/<int:id>/", methods=["GET", "POST", "DELETE"])
def movies(id=0):
    if request.method == "GET":

        if id:
            movie_obj = Movie.query.get(id)

            data = {
                "status": 200,
                "msg": "ok",
                "data": movie_obj.to_dict()
            }

            return jsonify(data)

        else:
            movie_list = Movie.query.all()

            movie_list_tran = []

            for movie in movie_list:
                movie_list_tran.append(movie.to_dict())

            data = {
                "status": 200,
                "msg": "ok",
                "data": movie_list_tran
            }

            return jsonify(data)
    elif request.method == "POST":

        if id:
            movie_obj = Movie.query.get(id)
            m_name = request.form.get("m_name")

            movie_obj.m_name = m_name

            db.session.add(movie_obj)

            db.session.commit()



        else:

            m_name = request.form.get("m_name")

            movie_obj = Movie()
            movie_obj.m_name = m_name

            db.session.add(movie_obj)
            db.session.commit()

        data = {
            "status": 201,
            "msg": "ok",
            "data": movie_obj.to_dict()
        }

        return jsonify(data)

    elif request.method == "DELETE":
        if id:
            movie_obj = Movie.query.get(id)

            db.session.delete(movie_obj)
            db.session.commit()

            data = {
                "status": 204,
                "msg": "delete success"
            }

            return jsonify(data)

