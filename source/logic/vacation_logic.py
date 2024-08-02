
from utils.dal_file import DAL
from models.vacation import VacationModel
from utils.image_handler import ImageHandler


class VacationLogic:
    """This class is responsible for handling all the business logic related to vacations."""

    def __init__(self):
        self.dal = DAL()

    def get_vacation_by_id(self, vacation_id: int):
        """Method to fetch a vacation by its ID"""
        try:
            sql = "SELECT v.vacationId, v.vacationInfo, c.countryName, v.vacationStart, v.vacationEnd, v.price, v.picName FROM project1.vacations AS v INNER JOIN project1.countries AS c ON v.countryId = c.countryId WHERE vacationId = %s LIMIT 1;"
            result = self.dal.get_table(sql, (vacation_id,))
            class_result = VacationModel.dicts_converter(VacationModel, result)
            return class_result
        except Exception as e:
            print(f"An error occurred while fetching vacation by ID: {e}")

    def get_all_vacations(self):
        """Method to fetch all vacations from the database"""
        try:
            sql = "SELECT v.vacationId, v.vacationInfo, c.countryName, v.vacationStart, v.vacationEnd, v.price, v.picName FROM project1.vacations AS v INNER JOIN project1.countries AS c ON v.countryId = c.countryId ORDER BY vacationStart ASC;"
            result = self.dal.get_table(sql)
            class_result = VacationModel.dicts_converter(VacationModel, result)
            return class_result
        except Exception as e:
            print("An error occurred while retrieving all vacations:", e)

    def insert_vacation(self, vacation: object):
        """Method to insert a new vacation into the database"""
        image_name = ImageHandler.save_image(vacation.pic_name)
        try:
            sql = "INSERT INTO project1.vacations (vacationId, vacationInfo, countryId, vacationStart, vacationEnd, price, picName) VALUES(%s,%s,%s,%s,%s,%s,%s);"
            result = self.dal.insert(sql, (vacation.vacation_id, vacation.vacation_info, vacation.country_id,
                                           vacation.vacation_start, vacation.vacation_end, vacation.price, image_name))
            return result
        except Exception as e:
            print("An error occurred while inserting vacation:", e)

    def update_vacation(self, vacation: object):
        """Method to update an existing vacation in the database"""
        try:
            old_image_name = self.get_old_image_name(vacation.vacation_id)
            image_name = ImageHandler.update_image(
                old_image_name, vacation.pic_name)
            sql = "UPDATE project1.vacations SET vacationInfo = %s,  countryId = %s ,  vacationStart = %s,  vacationEnd = %s , price = %s ,  picName = %s WHERE vacationId = %s;"
            result = self.dal.update(sql, (vacation.vacation_info, vacation.country_id, vacation.vacation_start,
                                     vacation.vacation_end, vacation.price, image_name, vacation.vacation_id))
            print("vacation updated successfully")
            return result
        except Exception as e:
            print("An error occurred while updating vacation:", e)

    def delete_vacation_by_id(self, vacation_id: int):
        """Method to delete a vacation by its ID from the database"""
        try:
            image_name = self.get_old_image_name(vacation_id)
            ImageHandler.delete_image(image_name)
            sql = "DELETE FROM project1.vacations WHERE vacationId = %s;"
            self.dal.delete(sql, (vacation_id,))
        except Exception as e:
            print("An error occurred while deleting vacation by ID:", e)

    def get_old_image_name(self, vacation_id: int):
        """Method to fetch the old image name of a vacation by its ID"""
        try:
            sql = "SELECT picName FROM project1.vacations WHERE vacationId = %s"
            result = self.dal.get_scalar(sql, (vacation_id,))
            return result["picName"]
        except Exception as e:
            print("An error occurred while fetching old image name:", e)
