import pygame, sys
from pygames.locals import *

FPS = 30
WINDOWWIDTH = 640
WINDOWHEIGHT = 480

def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

    pygame.display.set_caption('Asteroids Clone')

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
        # NEXT STEPS: create blank black screen for game ready screen

        pygame.display.update()
        FPSCLOCK.tick(FPS)
