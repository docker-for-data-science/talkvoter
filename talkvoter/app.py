from flask import Flask, render_template
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager
from .models import db, User, Talk, Vote
from .v1_resources import api_bp
from .config import Config
from . import views


application = Flask(__name__)
application.config.from_object(Config)

# initialize and create the database
db.init_app(application)
db.create_all(app=application)


admin = Admin(application, name='flask4data', template_mode='bootstrap3')
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Talk, db.session))
admin.add_view(ModelView(Vote, db.session))

login = LoginManager(application)
login.login_view = 'login'


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


@application.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


application.add_url_rule(r'/login/', view_func=views.login, methods=['GET', 'POST'])
application.add_url_rule(r'/logout/', view_func=views.logout, methods=['GET', 'POST'])
application.add_url_rule(r'/', view_func=views.dashboard, methods=['GET', 'POST'])

application.register_blueprint(
    api_bp,
    url_prefix="/api/v1")


if __name__ == "__main__":
    application.run(host='0.0.0.0', debug=True)
