from player import Player
from SnakeLadder.game.ComputerStrategy import ComputerStrategy


class ComputerPlayer(Player):
    def __init__(self, name, color, ComputerStrategy = ComputerStrategy()):
        super().__init__(name, color)
        self.ComputerStrategy = ComputerStrategy

