from flask import Flask, render_template
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from .models import db, Talk, Vote
from .v1_resources import api_bp
from .config import Config


application = Flask(__name__)
application.config.from_object(Config)

# initialize and create the database
db.init_app(application)
db.create_all(app=application)


admin = Admin(application, name='flask4data', template_mode='bootstrap3')
admin.add_view(ModelView(Talk, db.session))
admin.add_view(ModelView(Vote, db.session))


@application.route("/")
def index():
    name = "Python"
    return render_template('index.html', name=name)


@application.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


application.register_blueprint(
    api_bp,
    url_prefix="/api/v1")


if __name__ == "__main__":
    application.run(host='0.0.0.0', debug=True)
