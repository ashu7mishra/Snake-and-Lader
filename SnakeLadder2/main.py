from Game.snake import Snake
from Game.ladder import Ladder
import random

snakes = int(input("Enter number of snakes in the game: "))
snake_position = Snake(snakes).position_snakes()
print("snake_position", snake_position)

ladders = int(input("Enter number of ladders in the game: "))
ladder_position = Ladder(ladders).position_ladders()
print("ladder_position", ladder_position)

players = int(input("Specify number of players playing the game: "))
players_name = []
print("Specify players name")
for player in range(players):
    name = input(f"Enter player {player+1} name: ")
    players_name.append(name)
print(players_name)

if __name__ == "__main__":
    print("Let's start the game")

    player = False
    count = 0
    while True:
        print(f"Player {players_name[player]} turn")
        dice_roll = random.randint(1,6)
        print(f"Player {players_name[player]} throws: ", dice_roll)
        if dice_roll != 6:
            player = not(player)
        if count == 30:
            break
        count += 1

