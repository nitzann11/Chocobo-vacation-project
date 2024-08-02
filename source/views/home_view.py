from flask import Blueprint, render_template, session
from models.roles import RoleModel

home_blueprint = Blueprint('home_view', __name__)


@home_blueprint.route("/")
@home_blueprint.route("/home")
def home():
    return render_template('index.html', current_user=session.get("current_user"), user=RoleModel.USER.value, admin=RoleModel.ADMIN.value)
