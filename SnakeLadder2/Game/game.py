import random
from Game.snake import Snake
from Game.ladder import Ladder


class Game:
    def __init__(self, players, board_length, min_val, max_val):
        self.snakes = None
        self.ladders = None
        self.players = players
        self.board_length = board_length
        self.min_val = min_val
        self.max_val = max_val

    def get_snake_inputs(self):
        snakes = int(input("Enter number of snakes in the game: "))
        self.snakes = Snake(snakes)
        self.snake_position = self.snakes.position_snakes()
        print("snake_position", self.snake_position)

    def get_ladder_inputs(self):
        ladders = int(input("Enter number of ladders in the game: "))
        self.ladders = Ladder(ladders)
        self.ladder_position = self.ladders.position_ladders()
        print("ladder_position", self.ladder_position)

    def play(self):
        players_name_and_position = self.players.get_players_name_and_position()
        print("players_name", players_name_and_position)
        self.get_snake_inputs()
        self.get_ladder_inputs()

        print("************* LET'S BEGIN!!! ********************")
        
        player = 0
        while True:
            print(f"Player {players_name_and_position[player][0]} turn, current position: ", players_name_and_position[player][1])
            dice_roll = random.randint(self.min_val, self.max_val)
            
            if players_name_and_position[player][1] + dice_roll <= self.board_length:
                players_name_and_position[player][1] += dice_roll
                if players_name_and_position[player][1] == self.board_length:
                    print(f"Player {players_name_and_position[player][0]} moved to position: {self.board_length} and is the winner !!! ")
                    print("************ GAME OVER ****************")
                    print(f"*************** {players_name_and_position[player][0].upper()} WINS **************")
                    break
                
                if self.board_length - players_name_and_position[player][1] < self.min_val:
                    players_name_and_position[player][1] -= dice_roll
                    print(f"Player {players_name_and_position[player][0]} throws: ", dice_roll, " But canot move ")
                else:
                    print(f"Player {players_name_and_position[player][0]} throws: ", dice_roll, " and moved to position: ", players_name_and_position[player][1])

                snake_present = self.snakes.check_snake_position(players_name_and_position[player][1])
                if snake_present:
                    print(f"Snake present at {players_name_and_position[player][1]}, {players_name_and_position[player][0]} moved down to position {snake_present}")
                    players_name_and_position[player][1] = snake_present

                ladder_present = self.ladders.check_ladder_position(players_name_and_position[player][1])
                if ladder_present:
                    print(f"Ladder present at {players_name_and_position[player][1]}, {players_name_and_position[player][0]} moved up to position {ladder_present}")
                    players_name_and_position[player][1] = ladder_present
                    player -= 1

            if dice_roll != 6:
                player += 1
                if player == len(players_name_and_position):
                    player = 0
