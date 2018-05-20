from Item import Item
from Triangle import Triangle
from Point import Point
import math

class Car(Item):

    # X, Y
    def __init__(self, x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord
        self.speed = 0
        self.angle = 0
        self.available = True
        self.name = None
        self.score = 0
        self.checkPoint = 0
        self.startDistance = 0

    #Score
    def CalculateScore(self, checkLine, timePassed):
        p = Point(self.x, self.y)
        k = checkLine[self.checkPoint]
        distance = p.Distance(k)
        if self.startDistance == 0:
            self.startDistance = distance
        self.score = self.checkPoint*500 + 500 -(distance-3)/self.startDistance * 500 - timePassed
        if distance < 3:
            self.checkPoint = self.checkPoint+1
            self.startDistance = 0
        print(int(self.score))

    # Check is vehicle on the map
    def CheckAmIOnMap(self, map):
        for t in map.triangleObstacleList:
            if t.isInside(Point(self.x, self.y)):
                return False
        for t in map.triangleDotList:
            if t.isInside(Point(self.x, self.y)):
                return True
        return False

    # move self
    def Move(self, map):
        if self.CheckAmIOnMap(map):
            self.x += self.speed * math.cos(math.radians(self.angle))
            self.y += self.speed * math.sin(math.radians(self.angle))
        else:
            self.resetState(map)

    def resetState(self, map):
        self.speed = 0
        self.angle = 0
        self.x = map.startPosition.x
        self.y = map.startPosition.y


    '''
    TODO:
    1. Oblik vozila (slicica, strelica ili slicno...)
    2. Ograniciti da ne moze da ide u rikverc i da ne moze da se menja ugao kada se stoji
    3. Dodeljivanje random boje svakom vozilu
    '''