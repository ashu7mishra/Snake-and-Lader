from SnakeLadder.game.Game import Game
from SnakeLadder.games.Exception.Validation.InvalidBoardSizeException import InvalidBoardSizeException
from abc import ABC
from SnakeLadder.game.GameStats import GameStats
from SnakeLadder.game.players.player import Player
from SnakeLadder.games.snakeLadder.Elements.SnakeLadderGameElements import SnakeLadderGameElements


class Builder():
    def __init__(self):
        pass

    def snakes(self, no_of_snake):
        self.no_of_snake = no_of_snake
        return self

    def ladders(self, no_of_ladder):
        self.no_of_ladder = no_of_ladder
        return self

    def boardWidth(self, width_length):
        self.width_length = width_length
        return self

    def boardHeight(self, height_length):
        self.height_length = height_length
        return self

    def players(self, players):
        self.players = players
        return self

    def build(self):
        if(self.width_length < 3 or self.height_length < 3):
            return InvalidBoardSizeException("Invalid Board Dimensions")
        return SnakeLadderGame(self)


class SnakeLadderGame(Game):
    def __init__(self, Builder):
        super().__init__()
        self.gameStats = GameStats.WAITING_FOR_PLAYERS
        self.snakeCount = Builder.snakes()
        self.laddersCount = Builder.ladders()
        self.boardWidth = Builder.boardWidth()
        self.boardHeight = Builder.boardHeight()
        self.players = Builder.players()
        self.board = []
        self.element = SnakeLadderGameElements()

    def initialise(self):
        for i in range(self.boardWidth):
            temp = []
            for j in range(self.boardHeight):
                temp.append(None)
            self.board.append(temp)

        for s in range(self.snakeCount):
            self.element.append(SnakeFactory.getInstance().getRandomSnake(self.boardWidth, self.boardHeight))

        for l in range(self.laddersCount):
            self.element.append(LadderFactory.getInstance().getRandomSnake(self.boardWidth, self.boardHeight))



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




