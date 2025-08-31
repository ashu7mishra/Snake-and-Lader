from Game.players import Players
from Game.game import Game
from Game.dice import Dice


count_of_dice = Dice(int(input("Enter number of dice in the game: ")))
min_val, max_val = count_of_dice.get_min_and_max_number()
board_length = None
board_length = int(input("Enter the max length of board: ")) if not board_length else 100

players = int(input("Specify number of players playing the game: "))
players = Players(players)

if __name__ == "__main__":

    game = Game(players = players, board_length = board_length, min_val = min_val, max_val = max_val)
    game.play()
    