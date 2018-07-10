import pygame,os,time
from pygame.locals import *
import sys

def init_pygame(screen_size=(1280,720)):
    pygame.mixer.pre_init(44100,16,2,8192)
    pygame.init()   
    pygame.display.set_caption('希理的游戏2.0')
    pygame.mouse.set_visible(False)
    return pygame.display.set_mode(screen_size,0,32)