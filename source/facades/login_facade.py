from flask import request, session
from utils.cyber import Cyber
from models.user import UserModel
from models.roles import RoleModel
from models.credentials import Credentials
from models.client_error import ValidationError, AuthError
from logic.user_logic import UserLogic


class LoginFacade:
    """Class is responsible for managing user-related operations."""
    def __init__(self):
        self.bl = UserLogic()

    def register(self):
        """Method to register a new user"""
        user_first_name = request.form.get("first_name", type=str)
        user_last_name = request.form.get("last_name", type=str)
        user_email = request.form.get("email", type=str)
        user_password = request.form.get("password", type=str)
        user = UserModel(user_id=None, first_name=user_first_name, last_name=user_last_name,
                         email=user_email, password=user_password, role_id=RoleModel.USER.value)
        error = user.validate_user()
        if error:
            raise ValidationError("Register error", user)
        if self.bl.email_taken(user_email):
            raise ValidationError("Email already exists", user)
        user.password = Cyber.hash(user.password)
        self.bl.insert_user(user)
        del user.password

    def login(self):
        user_email = request.form.get("email", type=str)
        user_password = request.form.get("password", type=str)
        credentials = Credentials(user_email, Cyber.hash(user_password))
        error = credentials.validate()
        if error:
            raise ValidationError(error, credentials)
        user = self.bl.get_user_by_credentials(credentials)
        if not user:
            raise AuthError("Incorrect email or password", user)
        del user["password"]
        session["current_user"] = user

    def block_anon(self):
        """block access to anonymous users"""
        user = session.get("current_user")
        if not user:
            raise AuthError("You are not logged in")

    def block_none_admin(self):
        """Block access to everyone except admin"""
        user = session.get("current_user")
        if not user:
            raise AuthError("You are not logged in")
        print(user)
        if user["roleId"] != RoleModel.ADMIN.value:
            raise AuthError("You are not admin")

    def logout(self):
        """Method to logout the current user"""
        try:
            session.clear()
        except Exception as e:
            print(f"Error occurred while logging out: {e}")
