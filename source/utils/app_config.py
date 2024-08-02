from dotenv import load_dotenv
from os import environ

load_dotenv()

class AppConfig:
    development = environ.get("ENVIRONMENT") == "development"
    production = environ.get("ENVIRONMENT") == "production"
    mysql_host = environ.get("MYSQL_HOST")
    mysql_user = environ.get("MYSQL_USER")
    mysql_password = environ.get("MYSQL_PASSWORD")
    mysql_db = environ.get("MYSQL_DB")
    session_key = environ.get("SESSION_KEY")
    password_salt = environ.get("PASSWORD_SALT")

