from Player import Player
from Obstacle import Obstacle
from Map import Map
import time
import pygame
from pygame.constants import K_ESCAPE
import sys, os
from Point import Point

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
        self.player = Player("Test player", 890, 565)
        #self.obstacles.append(Obstacle(0,400,200,200))
        self.timePassed = 0
        self.done = False


    def generate_observations(self):
        return self.done, self.player.score, self.player, self.map.checkLines[self.player.checkPoint]

    #Move object(player) on map
    def Move(self):
        self.timePassed = self.timePassed + 0.03
        #time.sleep(0.1)
        self.done = self.player.Move(self.map)
        if(self.player.conscomands == 10):
            done = True
#        if self.isThereObstacle(self.map)[0] == True or self.isThereObstacle(self.map)[1] == True:
 #          print(self.isThereObstacle(self.map))
        return self.done


    # Check is point on the path
    def CheckPointOnMap(self, map, p):
        for t in map.TriangleList:
            if t.isInside(p):
                return True
        return False


    # is there obstacle on map
    def isThereObstacle(self, map):
        ind = [False, False, False]
        ind[0] = not self.CheckPointOnMap(self.map, self.player.frontCollisionLine[0])
        ind[1] = not self.CheckPointOnMap(self.map, self.player.frontCollisionLine[1])
        ind[2] = not self.CheckPointOnMap(self.map, self.player.frontCollisionLine[2])
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

        pygame.display.flip()


    # Get user input
    def GetInput(self):

        keystate = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT or keystate[K_ESCAPE]:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                self.player.speed += 0.5
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                self.player.speed -= 0.5
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                self.player.ChangeDirection(-1)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                self.player.ChangeDirection(1)


    def Score(self):
        #print(self.player.CalculateScore(self.map.checkLines, self.timePassed))
        return self.player.CalculateScore(self.map.checkLines, self.timePassed)

        '''
        TODO:
        1. klasa treba da je singlton klasa
        2. Jernostavni restart igre, start igre, pauza igre
        3. Unos imena igraca koji igra
        4. Mogucnost izora broja botova koji icestvuju u trci
        '''

