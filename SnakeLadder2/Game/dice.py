class Dice:
    def __init__(self, number_of_dice):
        self.number_of_dice = number_of_dice

    def get_min_and_max_number(self):
        return self.number_of_dice, self.number_of_dice*6