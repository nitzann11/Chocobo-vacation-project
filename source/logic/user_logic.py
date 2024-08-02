from utils.dal_file import DAL

class UserLogic:
    """  This class is responsible for handling user-related operations such as inserting, fetching, and validating users."""
    def __init__(self):
        self.dal = DAL()

    def insert_user(self, user: object):
        """Method to insert a new user into the database"""
        try:
            sql = "INSERT INTO project1.users (userId , firstName , lastName , email , password , roleId) VALUES(%s,%s,%s,%s,%s,%s);"
            result = self.dal.insert(sql, (user.user_id, user.first_name, user.last_name, user.email, user.password, user.role_id))
            print("User inserted successfully")
            return result
        except Exception as e:
            print(f"An error occurred while inserting user: {e}")

    def get_user_by_credentials(self, credentials: object):
        """Method to fetch a user by email and password"""
        try:
            sql = "SELECT * FROM project1.users WHERE email =%s AND password = %s;"
            user = self.dal.get_scalar(sql,(credentials.email, credentials.password,))
            return user
        except Exception as e:
            print(f"An error occurred while fetching user by credentials: {e}")

    def email_taken(self, email : str):
        try:
            sql = "SELECT EXISTS(SELECT * FROM project1.users WHERE email = %s) AS is_taken"
            result = self.dal.get_scalar(sql, (email,))
            return result["is_taken"] == 1
        except Exception as e:
            print(f"An error occurred while checking if email is taken: {e}")
