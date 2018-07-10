import pygame,os,time,sys
from pygame.locals import *

import read_setting as r
import utill as u

def make_font(message,color=(0,0,0),background = (100,100,100),antialias = False):
    surface = pygame.font.SysFont('arial',40).render(message,antialias,color,background)
    return surface

def main():
    screen_size = r.screen_size()
    screen = u.init_pygame(screen_size)

    opts = ('start','setting','exit')
    surface = []
    for n in opts:
        surface.append(make_font(r.language()[n]))
    #start_surface = make_font(r.language()['start'])
    #setting_surface = make_font(r.language()['setting'])
    #exit_surface = make_font(r.language()['exit'])

    choice = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()
                if event.key == K_DOWN:
                    pass

        screen.fill((255,255,255))
        for n,i in enumerate(surface):
            width = screen_size[0]//2-i.get_width()//2
            height = screen_size[1]//2-i.get_height()
            dest = (width,height)
            screen.blit(n,dest)
        pygame.display.update()
   



if __name__ == '__main__':
    main()