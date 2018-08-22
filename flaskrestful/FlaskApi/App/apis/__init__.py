from flask_restful import Api

from App.apis.BookApi import BookResource
from App.apis.CodeApi import CodeResource
from App.apis.MovieApi import MovieResource, MoviesResource
from App.apis.UserApi import UsersResource, UserResource

api = Api()


def init_api(app):
    api.init_app(app=app)


api.add_resource(MoviesResource, "/movies/")
api.add_resource(MovieResource, "/movies/<int:id>/")

api.add_resource(UsersResource, "/users/")
api.add_resource(UserResource, "/users/<int:id>/")

api.add_resource(BookResource, "/books/")

api.add_resource(CodeResource, "/codes/")

