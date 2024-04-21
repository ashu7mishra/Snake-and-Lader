from ValidationException import ValidationException

class InvalidBoardSizeException(ValidationException):

    def __init__(self, message):
        super().__init__(message)
