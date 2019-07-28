import flask

# from site.infra.view_modifiers import response

blueprint = flask.Blueprint('home', __name__, template_folder='templates')

@blueprint.route('/')
def index():
        # site/template is the default folder
        # pages are rendered with jinja2 from
        return flask.render_template('home/index.html')

@blueprint.route("/about")
def about():
    return flask.render_template('home/about.html')