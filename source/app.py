from flask import Flask, render_template
from views.home_view import home_blueprint
from views.vacations_view import vacations_blueprint
from views.login_view import auth_blueprint
from views.about_view import about_blueprint
from utils.app_config import AppConfig
from utils.logger import Logger

app = Flask(__name__)
app.secret_key = AppConfig.session_key

app.register_blueprint(home_blueprint)
app.register_blueprint(vacations_blueprint)
app.register_blueprint(auth_blueprint)
app.register_blueprint(about_blueprint)


@app.errorhandler(404)
def page_not_found(error):
    Logger.log(str(error))
    return render_template("404.html")


@app.errorhandler(Exception)
def catch_all(error):
    Logger.log(str(error))
    return render_template("500.html", error=error)
