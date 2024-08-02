from models.sql_table import SqlTable
from email_validator import validate_email
from models.roles import RoleModel


class UserModel(SqlTable):
    def __init__(self, user_id : int, first_name : str, last_name : str, email : str, password : str, role_id : int):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.role_id = role_id

    
    @staticmethod
    def _dict_converter(dictionary : dict):
        user_id = dictionary["userId"]   
        first_name = dictionary["firstName"]
        last_name = dictionary["lastName"]
        email = dictionary["email"]
        password = dictionary["password"]
        role_id = dictionary["roleName"]
        user = UserModel(user_id, first_name, last_name, email, password, role_id)
        return user
    
    def validate_user(self):
        validations = [
            (not self.first_name, "missing first name"),
            (not self.last_name, "missing last name"),
            (not self.email, "missing email"),
            (not self.password, "missing password"),
            (not self.role_id, "missing role id"),
            (len(self.first_name) < 2 or len(self.first_name) > 20, "name must be 2-20 characters (first name)"),
            (len(self.last_name) < 2 or len(self.last_name) > 20, "name must be 2-20 characters (last name)"),
            (len(self.email) < 2 or len(self.email) > 30, "email must be 2-30 characters"),
            (not validate_email(self.email), "Email not valid"),
            (len(self.password) < 4 or len(self.password) > 20, "Password must be 4-20 characters"),
            (self.role_id not in {RoleModel.ADMIN.value, RoleModel.USER.value}, "not valid role")
        ]

        for condition, error_message in validations:
            if condition:
                return error_message
        return None


    def __str__(self) -> str:
        return f"user ID: {self.user_id}, name: {self.first_name}, last name: {self.last_name}, email: {self.email}, password: {self.password}, role: {self.role_id}"


        
        