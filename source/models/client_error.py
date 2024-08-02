class ClientError(Exception):
    """Base class for custom exceptions raised by the client."""
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class ResourceNotFoundError(ClientError):
    """Exception raised when a resource is not found."""
    def __init__(self, id):
        super().__init__(f'{id} not found')
        self.id = id


class ValidationError(ClientError):
    """Exception raised when a validation error occurs."""
    def __init__(self, message,model):
        super().__init__(message)
        self.model = model


class AuthError(ClientError):
    """  Exception raised when an authentication error occurs."""
    def __init__(self, message,model = None):
        super().__init__(message)
        self.model = model

