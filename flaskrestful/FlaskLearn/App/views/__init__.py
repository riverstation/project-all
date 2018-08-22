from App.views.HelloView import hello


def init_views(app):
    app.register_blueprint(blueprint=hello)


