from models.sql_table import SqlTable
from datetime import date,datetime

class VacationModel(SqlTable):
    
    def __init__(self, vacation_id : int, vacation_info : str, country_id : int, vacation_start : date, vacation_end : date, price : int, pic_name : str):
        self.vacation_id = vacation_id
        self.vacation_info = vacation_info
        self.country_id = country_id
        self.vacation_start = vacation_start
        self.vacation_end = vacation_end
        self.price = price
        self.pic_name = pic_name


    @staticmethod
    def _dict_converter(dictionary : dict):
        vacation_id = dictionary["vacationId"]
        vacation_info = dictionary["vacationInfo"]
        country_id = dictionary["countryName"]
        vacation_start = dictionary["vacationStart"]
        vacation_end = dictionary["vacationEnd"]
        price = dictionary["price"]
        pic_name = dictionary["picName"]
        vacation = VacationModel(vacation_id, vacation_info, country_id, vacation_start, vacation_end, price, pic_name)
        return vacation
    


    def validate_create_vacation(self):
        today = datetime.today()
        vacation_start_input = datetime.strptime(self.vacation_start, '%Y-%m-%d')
        vacation_end_input = datetime.strptime(self.vacation_end, '%Y-%m-%d')
        validations = [
            (not self.country_id, "Country ID missing"),
            (not self.vacation_start, "Start date missing"),
            (not self.vacation_end, "End date missing"),
            (not self.price, "Price is missing"),
            (len(str(self.country_id)) < 1 or len(str(self.country_id)) > 2, "Country ID not valid"),
            (len(str(self.price)) < 1 or len(str(self.price)) > 5, "Price length not valid"),
            (self.price < 1 or self.price > 10000, "Price is not valid"),
            (vacation_start_input >= vacation_end_input, "Vacation start date should be before vacation end date"),
            (vacation_start_input <= today, "Vacation start date should be in the future")
        ]

        for condition, error_message in validations:
            if condition:
                return error_message
        return None


    def validate_edit_vacation(self):
        today = datetime.today()
        vacation_start_input = datetime.strptime(self.vacation_start, '%Y-%m-%d')
        vacation_end_input = datetime.strptime(self.vacation_end, '%Y-%m-%d')
        validations = [
            (not self.vacation_id, "Missing vacation ID"),
            (not self.country_id, "Country ID missing"),
            (not self.vacation_start, "Start date missing"),
            (not self.vacation_end, "End date missing"),
            (not self.price, "Price is missing"),
            (len(str(self.vacation_id)) < 1, "Vacation ID not valid"),
            (len(str(self.country_id)) < 1 or len(str(self.country_id)) > 2, "Country ID not valid"),
            (len(str(self.price)) < 1 or len(str(self.price)) > 5, "Price length not valid"),
            (self.price <= 0 or self.price > 10000, "Vacation price should be between 1 and 10000"),
            (vacation_start_input >= vacation_end_input, "Vacation start date should be before vacation end date"),
            ]
        
        
        for condition, error_message in validations:
            if condition:
                return error_message
        return None
        
        



    def __str__(self) -> str:
        return f"vacation ID: {self.vacation_id}, info: {self.vacation_info}, country id: {self.country_id}, vacation start: {self.vacation_start}, vacation end: {self.vacation_end}, price: {self.price}$, pic: {self.pic_name}"    
