import math

class Point:

    def __init__(self):
        self.x = 0
        self.y = 0

    def __init__(self, x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord

    def DistanceToDot(self, k):
        return math.sqrt((self.x - k.x)*(self.x - k.x)+(self.y - k.y)*(self.y - k.y))

    def Distance(self, line):
        return self.DistanceToDot(line[0]) + self.DistanceToDot(line[1]) - line[0].DistanceToDot(line[1])