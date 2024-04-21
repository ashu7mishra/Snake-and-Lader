from Game import Game
from GameStats import GameStats

class GameController:

    def __init__(self):
        self.game = Game()
        self.gamestats = GameStats()

    def startGame(self):
        self.game.initialise()
        while (not self.game.isOver()):
            player = self.game.getPlayerWithTurn()
            move = player.generateMove()
            while not self.game.isMoveValid(move):
                move = player.generateMove()
            self.game.makeMove(move)
        if self.game.isDraw():
            return "Game was a draw"
        else:
            winnerStats = self.gamestats.getWinningPlayerStats()
            return "Game was won: "+str(winnerStats)
