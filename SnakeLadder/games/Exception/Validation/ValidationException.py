from SnakeLadder.games.Exception.GameException import GameException


class ValidationException(GameException):
    
    def __init__(self):
        super().__init__()