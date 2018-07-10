# -*- coding: utf-8 -*-
import pygame,os,time,sys
from pygame.locals import *

import read_setting as r
import utill as u
import main
import chang_setting

def main():
    screen_size = r.screen_size()
    screen = u.init_pygame(screen_size)
    language_dir = r.language()
    opts = ('start','setting','exit')
    step = len(opts) + 1
    surface = []
    for n in opts:
        surface.append(u.make_font(language_dir[n]))
    #start_surface = u.make_font(r.language()['start'])
    #setting_surface = u.make_font(r.language()['setting'])
    #exit_surface = u.make_font(r.language()['exit'])

    choice = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()
                if event.key == K_DOWN:
                    if choice+1 < len(opts):
                        choice += 1
                if event.key == K_UP:
                    if choice > 0:
                        choice -= 1
                if event.key == K_RETURN:
                    if opts[choice] == 'start':
                        main.main()
                    if opts[choice] == 'setting':
                        chang_setting.main()
                    if opts[choice] == 'exit':
                        sys.exit()



        screen.fill((255,255,255))
        for n,i in enumerate(surface):
            width = screen_size[0]//2-i.get_width()//2
            height = screen_size[1]//step + n*(screen_size[1]//step)
            dest = (width,height)
            screen.blit(i,dest)
        
        for n,i in enumerate(opts):
            if choice == n:
                surface[n] = u.make_font(language_dir[i],background=(100,100,100))
            else:
                surface[n] = u.make_font(language_dir[i])

        pygame.display.update()
   



if __name__ == '__main__':
    main()