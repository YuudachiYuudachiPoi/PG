import pygame
from pygame.locals import *

screen_size=(1280,720)
pygame.init()
screen = pygame.display.set_mode(screen_size,0,32)
pygame.draw.rect(screen,(255,255,255),(100,100,100,100))
pygame.display.update()