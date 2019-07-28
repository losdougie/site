import flask

app = flask.Flask(__name__)

def main():
    register_blueprints()
    app.run(debug=True)

def register_blueprints():
    from views import home_views
    # from site.views import package_views

    app.register_blueprint(home_views.blueprint)
    # app.register_blueprint(package_views.blueprint)

if __name__ == '__main__':
    main()