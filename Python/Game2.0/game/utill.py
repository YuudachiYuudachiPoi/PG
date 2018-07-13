# -*- coding: utf-8 -*-
import pygame,os
from pygame.locals import *

def init_pygame(screen_size=(1280,720),mode=0):#0是窗口化
    pygame.mixer.pre_init(44100,16,2,8192)
    pygame.init()   
    pygame.display.set_caption('希理的游戏2.0')
    pygame.mouse.set_visible(False)
    
    return pygame.display.set_mode(screen_size,mode,32)

def make_font(message,background = None,color=(0,0,0),antialias = True,size=40):
    pwd = os.path.realpath(__file__)
    path_game = os.path.abspath(os.path.dirname(pwd)+os.path.sep+"..")
    f = open(path_game+'\data\setting.txt','r')
    font = pygame.font.Font(path_game+'\data\SIMSUN.TTC',size)
    #font = pygame.font.Font('SIMSUN.TTC',40)
    #font = pygame.font.SysFont('simsunnsimsun',40)
    surface = font.render(message,antialias,color,background)

    return surface

def render_block(screen,blocks):
    pass
