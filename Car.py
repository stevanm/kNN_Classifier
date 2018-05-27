from Item import Item
from Point import Point
import math
import os
import random
import pygame

class Car(Item):

    # X, Y
    def __init__(self, x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord
        self.speed = 4
        self.preAngle = 0
        self.angle = 0
        self.available = True
        self.name = None
        self.score = 0
        self.checkPoint = 0
        self.startDistance = 0
        self.__carList = list()
        self.carModels = self.createCarImageList()
        self.carModelPhoto = self.setCarModelPhoto()
        self.lastComand = 0
        self.conscomands = 0

        # Distance range used for collision detection
        self.frontCollisionLineDistance = 4
        self.frontDistanceRange = 4
        self.leftDistanceRange = 0.1
        self.rightDistanceRange = 0.1
        self.frontCollisionLine = list()
        self.frontCollisionLine.append(Point(0,0))
        self.frontCollisionLine.append(Point(0,0))
        self.frontCollisionLine.append(Point(0,0))

        #Score
    def CalculateScore(self, checkLine, timePassed):
        p = Point(self.x, self.y)
        k = checkLine[self.checkPoint]
        distance = p.Distance(k)
#        print(distance)
        if self.startDistance == 0:
            self.startDistance = distance
        #self.score = self.checkPoint*500 + 500 -(distance-20)/self.startDistance * 500 - timePassed
        if distance < 50:
            self.checkPoint = (self.checkPoint+1) % 22
            self.score = self.score + 1
            self.startDistance = 0
        return self.score
        #print(int(self.score))

    # Check is vehicle on the map
    def CheckAmIOnMap(self, map):
        for t in map.TriangleList:
            if t.isInside(Point(self.x, self.y)):
                return True
        return False

    def ChangeDirection(self, command):
        if(command == -1):
            if(self.lastComand == -1):
                self.conscomands = self.conscomands + 1
            else:
                self.conscomands = 0
            self.preAngle = self.angle
            self.angle -= 30
        if(command == 1):
            if(self.lastComand == 1):
                self.conscomands = self.conscomands + 1
            else:
                self.conscomands = 0
            self.preAngle = self.angle
            self.angle += 30

    # move self
    def Move(self, map):
        if self.CheckAmIOnMap(map):
            self.x += self.speed * math.cos(math.radians(self.angle))
            self.y += self.speed * math.sin(math.radians(self.angle))
            suc = False
        else:
            self.resetState(map)
            suc = True
        self.calculateFrontCollisionLine()
        return suc

    # Reset the car position (set it on the start)
    def resetState(self, map):
        self.speed = 1
        self.angle = 0
        self.x = map.startPosition.x
        self.y = map.startPosition.y
        self.score = 0
        self.checkPoint = 0

    # Create car image list
    def createCarImageList(self):
        for p in os.listdir("car_images"):
            self.__carList.append(p)


    # Choose the car photo (randomly selection)
    def setCarModelPhoto(self):
        carModelPhotoName = self.__carList[random.randint(0, len(self.__carList) - 1)]
        self.carModelPhoto = pygame.image.load(os.path.join('car_images', carModelPhotoName))
        transColor = self.carModelPhoto.get_at((0, 0))
        self.carModelPhoto.set_colorkey(transColor)
        carModelPathRect = self.carModelPhoto.get_rect()
        xCenter, yCenter =  carModelPathRect.center
        self.carModelPhoto = pygame.transform.scale(self.carModelPhoto, (40, 20))
        carModelPathRect.centerx = self.x
        carModelPathRect.centery = self.y
        return self.carModelPhoto

    # Is there obstacle in front od thr car
    def calculateFrontCollisionLine(self):
        dx = self.frontCollisionLineDistance * math.cos(math.radians(self.angle))
        dy = self.frontCollisionLineDistance * math.sin(math.radians(self.angle))
        x_middlePointOnFrontLine  = self.x + dx
        y_middlePointOnFrontLine = self.y + dy

        '''
        x_t1 = x_middlePointOnFrontLine + self.frontDistanceRange * math.cos(math.radians(self.angle))
        y_t1 = y_middlePointOnFrontLine + self.frontDistanceRange * math.sin(math.radians(self.angle))
        x_t2 = x_middlePointOnFrontLine + self.frontDistanceRange * math.cos(math.radians(self.angle))
        y_t2 = y_middlePointOnFrontLine + self.frontDistanceRange * math.sin(math.radians(self.angle))
        print(str(Point(x_t1, y_t1)))
        print(str(Point(x_t2, y_t2)))
        '''

        x_u = y_middlePointOnFrontLine - self.y
        y_u = self.x - x_middlePointOnFrontLine
        distU = math.sqrt(x_u * x_u + y_u * y_u)
        x_t1 = x_middlePointOnFrontLine + self.frontDistanceRange/2 * (x_u /distU)
        y_t1 = y_middlePointOnFrontLine + self.frontDistanceRange/2 * (y_u /distU)
        x_t2 = x_middlePointOnFrontLine - self.frontDistanceRange / 2 * (x_u / distU)
        y_t2 = y_middlePointOnFrontLine - self.frontDistanceRange / 2 * (y_u / distU)
        self.frontCollisionLine[0] = Point(x_t1, y_t1)
        self.frontCollisionLine[1] = Point(x_middlePointOnFrontLine, y_middlePointOnFrontLine)
        self.frontCollisionLine[2] = Point(x_t2, y_t2)

        dx = self.frontCollisionLineDistance * math.cos(math.radians(self.angle-30))
        dy = self.frontCollisionLineDistance * math.sin(math.radians(self.angle-30))
        x_middlePointOnFrontLine  = self.x + dx
        y_middlePointOnFrontLine = self.y + dy
        self.frontCollisionLine[0] = Point(x_middlePointOnFrontLine, y_middlePointOnFrontLine)

        dx = self.frontCollisionLineDistance * math.cos(math.radians(self.angle))
        dy = self.frontCollisionLineDistance * math.sin(math.radians(self.angle))
        x_middlePointOnFrontLine  = self.x + dx
        y_middlePointOnFrontLine = self.y + dy
        self.frontCollisionLine[1] = Point(x_middlePointOnFrontLine, y_middlePointOnFrontLine)

        dx = self.frontCollisionLineDistance * math.cos(math.radians(self.angle+30))
        dy = self.frontCollisionLineDistance * math.sin(math.radians(self.angle+30))
        x_middlePointOnFrontLine  = self.x + dx
        y_middlePointOnFrontLine = self.y + dy
        self.frontCollisionLine[2] = Point(x_middlePointOnFrontLine, y_middlePointOnFrontLine)
