from email_validator import validate_email


class Credentials():
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password

    def validate(self):
        validations = [
            (not self.email, "Missing email"),
            (not self.password, "missing password"),
            (not validate_email(self.email), "Email not valid")
        ]

        for condition, error_message in validations:
            if condition:
                return error_message
        return None
