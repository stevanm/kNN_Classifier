import pygame
from pygame.constants import K_ESCAPE

from GameController import *
import sys

def Draw():
    pygame.draw.circle(Surface, (255, 0, 0), (int(gc.player.x), int(600 - gc.player.y)), int(50))
    pygame.display.flip()

def GetInput():
    keystate = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keystate[K_ESCAPE]:
            pygame.quit()
            sys.exit()


if __name__ == '__main__':

    gc = GameController()

    pygame.init()
    Surface = pygame.display.set_mode((800,600))
    Surface.fill(pygame.Color(255,255,255))

    while True:
        GetInput()
        Draw()



