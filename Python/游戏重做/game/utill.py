import pygame
from pygame.locals import *

def init_pygame(screen_size=(1280,720)):
    pygame.mixer.pre_init(44100,16,2,8192)
    pygame.init()   
    pygame.display.set_caption('希理的游戏2.0')
    pygame.mouse.set_visible(False)
    
    return pygame.display.set_mode(screen_size,0,32)

def make_font(message,background = None,color=(0,0,0),antialias = False):
    surface = pygame.font.SysFont('arial',40).render(message,antialias,color,background)
    
    return surface