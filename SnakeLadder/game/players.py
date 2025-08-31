class Players:
    def __init__(self, players):
        self.players = players
        self.players_name_and_position = []

    def get_players_name_and_position(self):
        print("Specify players name")
        for player in range(self.players):
            name = input(f"Enter player {player+1} name: ")
            self.players_name_and_position.append([name, 0])
        return self.players_name_and_position