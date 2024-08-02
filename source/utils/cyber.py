from hashlib import sha512
from utils.app_config import AppConfig

class Cyber:
    @staticmethod
    def hash(password):
        encoded_password = password.encode("utf-8") + AppConfig.password_salt.encode("utf-8")
        hashed_password = sha512(encoded_password).hexdigest()
        return hashed_password