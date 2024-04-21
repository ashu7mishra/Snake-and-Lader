from SnakeLadder.game.players.player import Player
from abc import ABC

class Game(ABC):

    def __init__(self):
        print("Hello")

    def initialise(self):
        pass

    def isOver(self):
        pass

    def getPlayerWithTurn(self):
        return Player()

    def isMoveValid(self, move):
        pass

    def makeMove(self, move):
        pass

    def isADraw(self):
        pass

    def getWinningPlayerStats(self):
        pass