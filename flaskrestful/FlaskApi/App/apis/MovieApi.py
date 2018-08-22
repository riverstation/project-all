from flask_restful import Resource, reqparse, fields, marshal_with, marshal
from App.models.MovieModel import Movie

parser = reqparse.RequestParser()
parser.add_argument("movie_name", type=str)
# parser.add_argument("csrftoken", location="cookies")

movie_fields = {
    "m_name": fields.String
}

response_movie_fields = {
    "msg": fields.String(default="ok"),
    "status": fields.Integer,
    "data": fields.Nested(movie_fields)
}

response_movies_fields = {
    "msg": fields.String(default="ok"),
    "status": fields.Integer,
    "data": fields.List(fields.Nested(movie_fields))
}


class MovieResource(Resource):

    @marshal_with(response_movie_fields)
    def get(self, id=0):

        movie = Movie.query.get(id)

        data = {
            "msg": "ok",
            "status": 200,
            "data": movie
        }

        return data

    @marshal_with(response_movie_fields)
    def post(self, id=0):
        args = parser.parse_args()

        movie_id = id

        movie = Movie.query.get(movie_id)

        movie_name = args.get("movie_name")

        movie.m_name = movie_name

        movie.save()

        data = {
            "msg": "ok",
            "status": 200,
            "data": movie
        }

        return data

    def delete(self, id=0):
        movie_id = id

        movie = Movie.query.get(movie_id)

        movie.delete()

        data = {
            "status": "204",
            "msg": "delete ok"
        }

        return data


class MoviesResource(Resource):

    @marshal_with(response_movies_fields)
    def get(self):

        movies = Movie.query.all()

        data = {
            "msg": "ok",
            "status": 200,
            "data": movies
        }

        return data

    # @marshal_with(post_fields)
    def post(self):
        args = parser.parse_args()

        movie_name = args.get("movie_name")

        movie = Movie()
        movie.m_name = movie_name

        if movie.save():

            data = {
                "status": 201,
                "msg": "ok",
                "data": movie,
            }

            return marshal(data, response_movie_fields)
        else:
            return {"msg": "post ok but create fail"}
