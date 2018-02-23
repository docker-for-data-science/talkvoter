from flask import Flask, render_template
from .models import db
from .v1_resources import api_bp


application = Flask(__name__)
application.config.from_object('docker4data.settings')

# initialize and create the database
db.init_app(application)
db.create_all(app=application)


@application.route("/")
def hello():
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
