from models.sql_table import SqlTable
from models.roles import RoleModel


class LikeModel(SqlTable):

    def __init__(self, user_id : int, vacation_id : int):
        self.user_id = user_id
        self.vacation_id = vacation_id


    @staticmethod
    def _dict_converter(dictionary : dict):
        user_id = dictionary["userId"]   
        vacation_id = dictionary["vacationId"]
        like = LikeModel(user_id, vacation_id)
        return like


    def __str__(self) -> str:
        return f"user ID: {self.user_id}, Vacation ID: {self.vacation_id}"
    

    def validate_like(self):
        validations = [
            (not self.user_id, "missing user ID"),
            (not self.vacation_id, "missing Vacation ID")
        ]

        for condition, error_message in validations:
            if condition:
                return error_message
        return None