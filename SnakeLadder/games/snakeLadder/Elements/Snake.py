from SnakeLadder.games.snakeLadder.Elements.SnakeLadderGameElements import SnakeLadderGameElements


class Snake(SnakeLadderGameElements):

    def __init__(self, start, end):
        super().__init__()
        self.start = start
        self.end = end

    def getStart(self):
        return self.start

    def getEnd(self):
        return self.end