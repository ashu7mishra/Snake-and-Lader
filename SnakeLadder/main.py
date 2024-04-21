from SnakeLadder.game.players.humanplayer import HumanPlayer
from SnakeLadder.game.players.computerplayer import ComputerPlayer
from SnakeLadder.game.GameController import GameController
from SnakeLadder.games.GameFactory import GameFactory
from SnakeLadder.games.botStrategies.SnakeLadderStrategies import SimpleSnakeLadderStrategy


class Main:
    def __init__(self):
        players = list()
        players.append(HumanPlayer("Ashu", "Blue"))
        players.append(HumanPlayer("Abhi", "Red"))
        players.append(ComputerPlayer("Bot1", "Green", SimpleSnakeLadderStrategy()))
        game = GameFactory.getInstance().createClassicSnakeLadder(players)
        controller = GameController(game)
        controller.startGame()


if __name__ == '__main__':
    snake_and_Ladder = Main()
