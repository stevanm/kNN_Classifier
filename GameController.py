from Player import Player
from Obstacle import Obstacle
from Map import Map
import time
import pygame
from pygame.constants import K_ESCAPE
import sys

class GameController:

    obstacles = []

    def __init__(self):

        pygame.init()
        self.Surface = pygame.display.set_mode((800, 600))
        self.Surface.fill(pygame.Color(255, 255, 255))

        self.player = Player("Test player", 100, 500)
        self.obstacles.append(Obstacle(0,400,200,200))
        self.map = Map()

    def Move(self):
        time.sleep(0.030)
        self.player.Move(self.map)


    def Draw(self):
        pygame.draw.rect(self.Surface, pygame.Color(0,255,0), (0,400, 200,200))
        pygame.draw.circle(self.Surface, (255, 0, 0), (int(self.player.x), int(self.player.y)), int(20))
        pygame.display.flip()

    # get user input
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
                self.player.angle += 30
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                self.player.angle -= 30

        '''
        TODO:
        1. klasa treba da je singlton klasa
        2. Jernostavni restart igre, start igre, pauza igre
        3. Unos imena igraca koji igra
        4. Mogucnost izora broja botova koji icestvuju u trci
        '''


