import pygame,os,time,sys
from pygame.locals import *

def make_font(message,color=(0,0,0),background = None,antialias = False):
    surface = pygame.font.SysFont('arial',40).render(message,antialias,color,background)
    return surface

def init_pygame(screen_size=(1280,720)):
    pygame.mixer.pre_init(44100,16,2,8192)
    pygame.init()   
    pygame.display.set_caption('希理的游戏2.0')
    pygame.mouse.set_visible(False)
    return pygame.display.set_mode(screen_size,0,32)

def main():
    
    screen = init_pygame()

    start_surface = make_font('start',color=(0,0,0),background=(100,100,100))
    exit
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == ESC:
                    sys.exit()
                
        
        screen.fill((255,255,255))

   



if __name__ == '__main__':
    main()