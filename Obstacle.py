from Item import Item

class Obstacle(Item):

    # X, Y
    def __init__(self, x1_coord, y1_coord, x2_coord, y2_coord):
        self.x1 = x1_coord
        self.y1 = y1_coord
        self.x2 = x2_coord
        self.y2 = y2_coord
