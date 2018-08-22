from App.views.MovieView import movie
from App.views.UserView import user


def init_views(app):
    app.register_blueprint(blueprint=user)
    app.register_blueprint(blueprint=movie)


