class Snake:
    def __init__(self, snakes):
        self.snakes = snakes
        self.snake_position = []

    def position_snakes(self):
        print("Specificy snake tail and head in following manner for all snakes: (tail head) \n")
        for snake in range(self.snakes):
            pos = input(f"Enter snake {snake+1} tail and head: ")
            pos = pos.split()
            self.snake_position.append([int(pos[0]), int(pos[1])])
        return self.snake_position
    
    def check_snake_position(self, position):
        for pos in self.snake_position:
            if pos[1] == position:
                return pos[0]
        return None