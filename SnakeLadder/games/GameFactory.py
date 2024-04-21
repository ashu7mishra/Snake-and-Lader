from abc import ABCMeta, abstractmethod
from snakeLadder.SnakeLadderGame import SnakeLadderGame

class Factory(metaclass=ABCMeta):

    @staticmethod
    def create_game():
        "implement in child class"
class GameFactory:
    __INSTANCE = None

    @staticmethod
    def getInstance():
        if GameFactory().__INSTANCE == None:
            GameFactory().__INSTANCE = GameFactory()
        return GameFactory().__INSTANCE

    def createClassicSnakeLadder(self, players):
        return SnakeLadderGame.Builder(100, 5, 9)
