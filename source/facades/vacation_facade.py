from flask import request,flash
from models.vacation import VacationModel
from models.client_error import ResourceNotFoundError, ValidationError
from logic.vacation_logic import VacationLogic


class VacationFacade:
    """Class is responsible for managing vacation-related operations."""

    def __init__(self):
        self.bl = VacationLogic()

    def create_vacation(self):
        """Method to create a new vacation"""

        vacation_info = request.form.get('vacation_info', type=str)
        country_id = request.form.get('country_id', type=int)
        vacation_start = request.form.get('vacation_start', type=str)
        vacation_end = request.form.get('vacation_end', type=str)
        vacation_price = request.form.get('vacation_price', type=int)
        pic_name = request.files.get('add_image')

        vacation = VacationModel(vacation_id=None, vacation_info=vacation_info, country_id=country_id,
                                 vacation_start=vacation_start, vacation_end=vacation_end,
                                 price=vacation_price, pic_name=pic_name)
        error = vacation.validate_create_vacation()
        if error:
            raise ValidationError(error)
        self.bl.insert_vacation(vacation)
        flash("Vacation has been added!✈️", "success")
        return vacation

    def update_existing_vacation(self):
        """Method to update an existing vacation"""
        vacation_id = request.form.get('vacation_id', type=int)
        vacation_info = request.form.get('vacation_info')
        country_id = request.form.get('country_id', type=int)
        vacation_start = request.form.get('vacation_start')
        vacation_end = request.form.get('vacation_end')
        vacation_price = request.form.get('vacation_price', type=int)
        pic_name = request.files.get('add_image')
        vacation = VacationModel(vacation_id=vacation_id, vacation_info=vacation_info, country_id=country_id,
                                    vacation_start=vacation_start, vacation_end=vacation_end,
                                    price=vacation_price, pic_name=pic_name)
        error = vacation.validate_edit_vacation()
        if error:
            raise ValidationError(error)
        self.bl.update_vacation(vacation)
        return vacation

    def delete_vacation(self, vacation_id: int):
        """Method to delete a vacation"""
        self.bl.delete_vacation_by_id(vacation_id)
        flash("Vacation has been removed.🚮", "success")


    def show_all_vacations(self):
        vacations = self.bl.get_all_vacations()
        return vacations

    def get_vacation_using_id(self, vacation_id: int):
        """Method to fetch a vacation by its ID"""
        result = self.bl.get_vacation_by_id(vacation_id)
        if not result:
            raise ResourceNotFoundError(vacation_id)
        return result[0]
