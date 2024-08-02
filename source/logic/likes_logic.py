from utils.dal_file import DAL
from models.like import LikeModel


class LikeLogic:
    """ This class provides methods for interacting with the 'likes' table in the database."""

    def __init__(self):
        self.dal = DAL()

    def get_all_likes_by_user_id(self, user_id: int):
        """Method to fetch all likes of specific user from the database"""
        try:
            sql = "SELECT * FROM project1.likes WHERE userId = %s; "
            result = self.dal.get_table(sql, (user_id,))
            class_result = LikeModel.dicts_converter(LikeModel, result)
            return class_result
        except Exception as e:
            print("An error occurred while retrieving likes:", e)

    def get_like_counts_for_all_vacations(self):
        """Method to fetch like counts for all vacations."""
        try:
            sql = "SELECT vacationId, COUNT(*) AS like_count FROM project1.likes GROUP BY vacationId;"
            results = self.dal.get_table(sql)
            like_counts = {result['vacationId']: result['like_count'] for result in results}
            return like_counts
        except Exception as e:
            print("An error occurred while retrieving like counts:", e)

    def insert_like(self, like: object):
        """Method to insert a new like into the database"""
        try:
            sql = "INSERT INTO project1.likes (userId, vacationId) VALUES (%s, %s);"
            self.dal.insert(sql, (like.user_id, like.vacation_id))
            print("Like inserted successfully.")
        except Exception as e:
            print("An error occurred while inserting like:", e)

    def delete_like(self, like: object):
        """Method to delete a like from the database"""
        try:
            sql = "DELETE FROM project1.likes WHERE userId = %s AND vacationId = %s;"
            self.dal.delete(sql, (like.user_id, like.vacation_id))
            print("Like deleted successfully.")
        except Exception as e:
            print("An error occurred while deleting like:", e)

    def like_exists(self, like: object):
        """Method to check if a like exists in the database"""
        try:
            sql = "SELECT EXISTS(SELECT * FROM project1.likes WHERE userId = %s AND vacationId = %s) AS is_liked"
            result = self.dal.get_scalar(sql, (like.user_id, like.vacation_id))
            return result["is_liked"] == 1
        except Exception as e:
            print("An error occurred while deleting like:", e)
