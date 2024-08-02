from datetime import datetime
from flask import session

class Logger:
    __log_file = "./logger.log"

    @staticmethod
    def log(message : str):
        """ method to write a message to the log file for logging"""
        now = datetime.now()
        user = session.get("current_user")

        with open(Logger.__log_file, "a") as file:
            file.write(str(now) + "\n")
            file.write(message + "\n")

            user = session.get("current_user")
            if user:
                file.write("user ID : " + str(user["userId"]) + ", User email: " + user["email"] + "\n")
                file.write("----------------------------------------------------------------------------" + "\n")

