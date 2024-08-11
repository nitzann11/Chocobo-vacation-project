from flask import request, flash
from logic.likes_logic import LikeLogic
from models.client_error import AuthError
from models.like import LikeModel


class LikeFacade:
    """Class is responsible for managing like-related operations."""

    def __init__(self):
        self.bl = LikeLogic()

    def get_likes_count(self):
        """Method to fetch a like by its user ID"""
        like_counts = self.bl.get_like_counts_for_all_vacations()
        return like_counts

    def get_likes_using_user_id(self, user_id: int):
        """Method to fetch all likes by user ID."""
        result = self.bl.get_all_likes_by_user_id(user_id)
        return result

    def create_like(self):
        """Method to insert a new like into the database"""
        user_id = request.form.get('user_id', type=int)
        vacation_id = request.form.get('vacation_id', type=int)
        like = LikeModel(user_id=user_id, vacation_id=vacation_id)
        error = like.validate_like()
        if error:
            raise AuthError(error)
        self.bl.insert_like(like)
        flash("Like has been Added!❤️", "success")
        return like

    def remove_like(self):
        """Method to remove a like from the database"""
        user_id = request.form.get('user_id', type=int)
        vacation_id = request.form.get('vacation_id', type=int)
        like = LikeModel(user_id=user_id, vacation_id=vacation_id)
        error = like.validate_like()
        if error:
            raise AuthError(error)
        self.bl.delete_like(like)
        flash("Like has been removed!💔", "success")
        return "Like removed successfully"

    def create_or_delete_like(self):
        """Method that gets response from the database about like existence and responds accordingly to create or delete."""
        user_id = request.form.get('user_id', type=int)
        vacation_id = request.form.get('vacation_id', type=int)
        like = LikeModel(user_id=user_id, vacation_id=vacation_id)
        exists = self.bl.like_exists(like)
        if exists == True:
            return self.remove_like()
        else:
            return self.create_like()
