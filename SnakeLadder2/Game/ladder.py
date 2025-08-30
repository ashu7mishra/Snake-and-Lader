class Ladder:
    def __init__(self, ladders):
        self.ladders = ladders
        self.ladder_position = []

    def position_ladders(self):
        print("Specificy ladders start and end positions in following manner for all ladders: (start end) \n")
        for ladder in range(self.ladders):
            pos = input(f"Enter ladder {ladder+1} start and end: ")
            pos = pos.split()
            self.ladder_position.append([int(pos[0]), int(pos[1])])
        return self.ladder_position