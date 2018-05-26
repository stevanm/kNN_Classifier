from Item import Item
from Triangle import Triangle
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
        self.speed = 0
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

    #Score
    def CalculateScore(self, checkLine, timePassed):
        p = Point(self.x, self.y)
        k = checkLine[self.checkPoint%4]
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
        for t in map.TriangleList:
            if t.isInside(Point(self.x, self.y)):
                return True
        return False

    def ChangeDirection(self, command):
        if(command == 1):
            self.preAngle = self.angle
            self.angle -= 30
        if(command == 2):
            self.preAngle = self.angle
            self.angle += 30

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
        self.score = 0
        self.checkPoint = 0

    # Create car image list
    def createCarImageList(self):
        for p in os.listdir("car_images"):
            self.__carList.append(p)



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

    '''
    TODO:
    1. Oblik vozila (slicica, strelica ili slicno...)
    '''