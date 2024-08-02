import mysql.connector
from utils.app_config import AppConfig


# Data Access Layer (DAL) for MySQL database operations.
class DAL:
    """Class for interacting with MySQL database"""

    def __init__(self):
        """Establish connection to the MySQL database"""
        try:
            self.connection = mysql.connector.connect(
                # localhost = current machine.
                host=AppConfig.mysql_host, user=AppConfig.mysql_user, password=AppConfig.mysql_password, database=AppConfig.mysql_db)
        except mysql.connector.Error as e:
            print(f"Error connecting to MySQL: {e}")

    def get_table(self, sql: str, params: tuple = None):
        """Establish connection to the MySQL database"""
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute(sql, params)
                table = cursor.fetchall()
                return table
        except mysql.connector.Error as e:
            print(f"Error executing SQL query: {e}")

    def get_scalar(self, sql: str, params: tuple = None):
        """Method to execute a SQL query that returns a single scalar value"""
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute(sql, params)
                table = cursor.fetchone()
                return table
        except mysql.connector.Error as e:
            print(f"Error executing SQL query: {e}")

    def insert(self, sql: str, params: tuple = None):
        """Method to execute an INSERT SQL query"""
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql, params)
                self.connection.commit()  # Save to database now.
                last_row_id = cursor.lastrowid
                return last_row_id
        except mysql.connector.Error as e:
            print(f"Error executing SQL query: {e} ")

    def update(self, sql: str, params: tuple = None):
        """Method to execute an UPDATE SQL query"""
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql, params)
                self.connection.commit()  # Save to database now.
                row_count = cursor.rowcount
                return row_count
        except mysql.connector.Error as e:
            print(f"Error executing SQL query: {e}")

    def delete(self, sql: str, params: tuple = None):
        """Method to execute a DELETE SQL query"""
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql, params)
                self.connection.commit()  # Save to database now.
                row_count = cursor.rowcount
                return row_count
        except mysql.connector.Error as e:
            print(f"Error executing SQL query: {e}")

    def close(self):
        """Method to close the connection to the MySQL database"""
        try:
            self.connection.close()
        except mysql.connector.Error as e:
            print(f"Error closing MySQL connection: {e}")
