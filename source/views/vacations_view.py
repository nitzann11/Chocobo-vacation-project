from flask import Blueprint,render_template,send_file,redirect,url_for,request,session
from facades.vacation_facade import VacationFacade
from facades.login_facade import LoginFacade
from facades.like_facade import LikeFacade
from utils.image_handler import ImageHandler
from utils.logger import Logger
from models.client_error import ResourceNotFoundError,ValidationError, AuthError
from models.roles import RoleModel
from models.countries import CountryModel


vacations_blueprint = Blueprint('vacations_view', __name__)
facade = VacationFacade()
login_facade = LoginFacade()
like_facade = LikeFacade()

@vacations_blueprint.route("/vacations", methods=["GET", "POST"])
def list():
    try:
        login_facade.block_anon()
        all_vacations = facade.show_all_vacations()
        like_count = like_facade.get_likes_count()
        current_user = session.get("current_user")


        user_liked_vacations = []
        if current_user:
            user_likes = like_facade.get_likes_using_user_id(current_user['userId'])
            user_liked_vacations = [like.vacation_id for like in user_likes]

        if request.method == "GET": return render_template('vacations.html', vacations=all_vacations,likes = like_count, user_liked_vacations=user_liked_vacations , current_user = current_user, admin = RoleModel.ADMIN.value, user = RoleModel.USER.value)
        like_facade.create_or_delete_like()
        return redirect(url_for("vacations_view.list"))
    except AuthError as err:
        Logger.log(err.message)
        return redirect(url_for("login_view.login", error=err.message))

@vacations_blueprint.route("/vacations/images/<string:image_name>")
def get_image(image_name):
    image_path = ImageHandler.get_image_path(image_name)
    return send_file(image_path)
    


@vacations_blueprint.route("/vacations/details/<int:vacation_id>")
def details(vacation_id):
    try:
        one_vacation = facade.get_vacation_using_id(vacation_id)
        return render_template('vacation_details.html', vacation=one_vacation, current_user = session.get('current_user'), admin = RoleModel.ADMIN.value )
    except ResourceNotFoundError as err:
        Logger.log(err.message)
        return render_template("404.html",error=err.message)

@vacations_blueprint.route("/vacations/new",methods=["GET","POST"])
def insert():
    try:
        login_facade.block_anon()
        login_facade.block_none_admin()
        if (request.method=="GET"): return render_template("insert_vacation.html", current_user = session.get('current_user'), countries = CountryModel)
        facade.create_vacation()
        return redirect(url_for("vacations_view.list"))
    except AuthError as err:
        return render_template("500.html",error=err.message)
    except ValidationError as err:
        return render_template("insert_vacation.html", error=err.message)
 


@vacations_blueprint.route("/vacations/edit/<int:vacation_id>",methods=["GET","POST"])
def edit(vacation_id):
    try:
        login_facade.block_anon()
        login_facade.block_none_admin()
        if(request.method=="GET"):
            one_vacation = facade.get_vacation_using_id(vacation_id)
            return render_template("edit_vacation.html", vacation=one_vacation,  current_user = session.get('current_user'),  countries = CountryModel)
        
        facade.update_existing_vacation()
        return redirect(url_for("vacations_view.list"))
    except AuthError as err:
        return render_template("500.html",error=err.message)
    except ValidationError as err:
        return render_template("edit_vacation.html", error=err.message)


@vacations_blueprint.route("/vacations/delete/<int:vacation_id>",methods=["GET","POST"])
def delete(vacation_id):
    login_facade.block_anon()
    login_facade.block_none_admin()
    try:
        login_facade.block_none_admin()
        facade.delete_vacation(vacation_id)
        return redirect(url_for("vacations_view.list"))
    except AuthError as err:
        return render_template("500.html",error=err.message)


