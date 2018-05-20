from Item import Item

class Obstacle(Item):

    # X, Y
    def __init__(self, x1_coord, y1_coord, dx, dy):
        self.x1 = x1_coord
        self.y1 = y1_coord
        self.dx = dx
        self.dy = dy
