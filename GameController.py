from Player import Player
from Bot import Bot
from Map import Map
import time
import pygame
from pygame.constants import K_ESCAPE
import sys, os
from Point import Point
from random import randint

class GameController:

    obstacles = []


    def __init__(self):

        #Before pygame initialization, center the game window on screen
        os.environ['SDL_VIDEO_CENTERED'] = '1'

        pygame.init()
        pygame.display.set_caption('Machine Learning Smarter')
        #self.winWidth, self.winHeight = self.bgPhoto.get_rect().size #game window size == photo size
        self.winWidth = 1600
        self.winHeight = 668
        self.map = Map(1600,668)
        self.Surface = pygame.display.set_mode((self.winWidth, self.winHeight))
        self.Surface.fill(pygame.Color(255, 255, 255))
        self.player = Player("Test player", 890, 565, 1, self.map.checkLines)
        #self.player.angle = randint(0,360)

        self.bot = Bot("Test player", 890, 565, 1, self.map.checkLines)
        #self.bot.angle = randint(0,360)
        self.timePassed = 0
        self.done = False


    def generate_observations(self):
        return self.done, self.player.score, self.player, self.map.checkLines[self.player.checkPoint]

    #Move object(players) on map
    def Move(self):
        self.timePassed = self.timePassed + 0.03
 #       time.sleep(0.5)
        self.done = self.player.Move(self.map)
        self.bot.Move(self.map)
        if(self.player.conscomands == 10):
            done = True
        return self.done


    # Check is point on the path
    def CheckPointOnMap(self, map, p, bot):
        ins = False
        for t in map.TriangleList:
            if t.isInside(p):
                ins = True
        if ins:
            ins = p.DistanceToDot(Point(bot.x,bot.y)) > 25
        return ins


    # is there obstacle on map
    def isThereObstacle(self, map):
        ind = [False, False, False]
        ind[0] = not self.CheckPointOnMap(self.map, self.player.frontCollisionLine[0], self.bot)
        ind[1] = not self.CheckPointOnMap(self.map, self.player.frontCollisionLine[1], self.bot)
        ind[2] = not self.CheckPointOnMap(self.map, self.player.frontCollisionLine[2], self.bot)
        return ind


    #Draw the scene
    def Draw(self):

        bgPhoto = pygame.image.load('path/race_path.jpg')  # background photo
        # Draw background photo
        bgPhotoScaled = pygame.transform.scale(bgPhoto, (self.winWidth, self.winHeight))
        self.Surface.blit(bgPhotoScaled, (0,0))

        # Draw player car
        carModel = pygame.transform.rotate(self.player.carModelPhoto, -self.player.angle)
        self.Surface.blit(carModel,(int(self.player.x)-20, int(self.player.y)-10))

        botModel = pygame.transform.rotate(self.bot.carModelPhoto, -self.bot.angle)
        self.Surface.blit(botModel,(int(self.bot.x)-20, int(self.bot.y)-10))

        pygame.display.flip()


    # Get user input
    def GetInput(self):

        keystate = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT or keystate[K_ESCAPE]:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                self.bot.speed += 0.5
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                self.bot.speed -= 0.5
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                self.bot.ChangeDirection(-1)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                self.bot.ChangeDirection(1)


    def Score(self):
        return self.player.CalculateScore(self.map.checkLines, self.timePassed)
