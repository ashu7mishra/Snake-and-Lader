from Game.snake import Snake
from Game.ladder import Ladder
from Game.players import Players
from Game.game import Game
from Game.dice import Dice
import random

snakes = int(input("Enter number of snakes in the game: "))
snakes = Snake(snakes)
snake_position = snakes.position_snakes()
print("snake_position", snake_position)

ladders = int(input("Enter number of ladders in the game: "))
ladders = Ladder(ladders)
ladder_position = ladders.position_ladders()
print("ladder_position", ladder_position)

players = int(input("Specify number of players playing the game: "))
players_name_and_position = Players(players).get_players_name_and_position()
print("players_name", players_name_and_position)

count_of_dice = Dice(int(input("Enter number of dice in the game: ")))
board_length = None
board_length = int(input("Enter the max length of board: ")) if not board_length else 100

if __name__ == "__main__":
    print("Let's start the game")

    game = Game(snakes = snake_position, ladders = ladder_position, players = players_name_and_position)
    min_val, max_val = count_of_dice.get_min_and_max_number()
    player = 0
    # count = 0
    while True:
        print(f"Player {players_name_and_position[player][0]} turn, current position: ", players_name_and_position[player][1])
        dice_roll = random.randint(min_val, max_val)
        
        if players_name_and_position[player][1] + dice_roll <= 100:
            players_name_and_position[player][1] += dice_roll
            print(f"Player {players_name_and_position[player][0]} throws: ", dice_roll, " and moved to position: ", players_name_and_position[player][1])

            snake_present = snakes.check_snake_position(players_name_and_position[player][1])
            if snake_present:
                print(f"Snake present at {players_name_and_position[player][1]}, {players_name_and_position[player][0]} moved down to position {snake_present}")
                players_name_and_position[player][1] = snake_present

            ladder_present = ladders.check_ladder_position(players_name_and_position[player][1])
            if ladder_present:
                print(f"Ladder present at {players_name_and_position[player][1]}, {players_name_and_position[player][0]} moved up to position {ladder_present}")
                players_name_and_position[player][1] = ladder_present
                player -= 1
            
            if players_name_and_position[player][1] == 100:
                print(f"Player {players_name_and_position[player][0]} moved to position: 100 and is the winner !!! ")
                print("************ GAME OVER ****************")
                print(f" {players_name_and_position[player][0].upper()} WINS")
                break
        if dice_roll != 6:
            player += 1
            if player == len(players_name_and_position):
                player = 0 
        # if count == 30:
        #     break
        # count += 1

