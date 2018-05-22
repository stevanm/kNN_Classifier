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
        self.carModels = self.createCarImageList()
        self.carModelPhoto = self.setCarModelPhoto()

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

    # Create car image list
    def createCarImageList(self):
        self.__carList = list()
        for p in os.listdir("car_images"):
            self.__carList.append(p)
        print(self.__carList)


    def setCarModelPhoto(self):
        carModelPhotoName = self.__carList[random.randint(0, len(self.__carList) - 1)]
        self.carModelPhoto = pygame.image.load(os.path.join('car_images', carModelPhotoName))
        carModelPathRect = self.carModelPhoto.get_rect()
        xCenter, yCenter =  carModelPathRect.center
        self.carModelPhoto = pygame.transform.scale(self.carModelPhoto, (70, 35))
        carModelPathRect.centerx = self.x
        carModelPathRect.centery = self.y
        return self.carModelPhoto

    #BUG: Prilikom rotacije uvecava se obuhvat oko automobila
    '''
    def rotateCarModelPhoto(self, angle):
        carModelPathRect = self.carModelPhoto.get_rect()
        xOldCenter, yOldCenter = carModelPathRect.center
        self.carModelPhoto = pygame.transform.rotate(self.carModelPhoto,self.angle)
        carModelPathRect.centerx = xOldCenter
        carModelPathRect.centery = yOldCenter
        return self.carModelPhoto
       '''




    '''
    TODO:
    1. Oblik vozila (slicica, strelica ili slicno...)
    3. Dodeljivanje random boje svakom vozilu
    '''