from flask import Blueprint, render_template, url_for, redirect, request
from facades.login_facade import LoginFacade
from models.client_error import ValidationError, AuthError
from utils.logger import Logger


auth_blueprint = Blueprint("login_view", __name__)

facade = LoginFacade()


@auth_blueprint.route("/register", methods=["GET", "POST"])
def register():
    try:
        if request.method == "GET":
            return render_template("register.html")
        facade.register()
        return redirect(url_for("home_view.home"))
    except ValidationError as err:
        Logger.log(err.message)
        return render_template("register.html", error=err.message, user=err.model)


@auth_blueprint.route("/login", methods=["GET", "POST"])
def login():
    error = request.args.get('error')
    try:
        if request.method == "GET":
            return render_template("login.html", credentials={}, error=error)
        facade.login()
        return redirect(url_for("vacations_view.list"))
    except (ValidationError, AuthError) as err:
        Logger.log(err.message)
        return render_template("login.html", error=err.message, credentials=err.model)


@auth_blueprint.route("/logout", methods=["GET", "POST"])
def logout():
    facade.logout()
    return redirect(url_for("home_view.home"))
