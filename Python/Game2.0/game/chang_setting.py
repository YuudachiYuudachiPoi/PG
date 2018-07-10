# -*- coding: utf-8 -*-
import pygame,os,time,sys
from pygame.locals import *

import read_setting as r
import utill as u
import menu

def opt_opts(opt):
    if opt == 'language':
        opt_choices = ('Chinese','English')
    elif opt == 'resolution':
        opt_choices = ('1280,720',
                '1920,1080')
    elif opt == 'full screen':
        opt_choices = ('Enable',
                'Disable')
    elif opt == 'exit':
        opt_choices = ('')
    return opt_choices

def write_file(file):
    pwd = os.path.realpath(__file__)
    path_game = os.path.abspath(os.path.dirname(pwd)+os.path.sep+"..")
    f = open(path_game+'\data\setting.txt','w')
    remarks = ('#language',
               '#screen_size',
               '#full_screen',
               '#last_line')
    for n,i in enumerate(file):
        message = '{:<30}{}'.format(i,remarks[n])+'\n'
        f.write(message)


def main(screen):
    screen_size = r.screen_size()
    language_dir = r.language()
    opts = ('language','resolution','full screen','exit')
    step = len(opts) + 1
    surface = []
    file = r.read_file()
    for n,i in enumerate(opts):
        if i == 'exit':
            message = '{:<10}{:>10}'.format(language_dir[i],file[n])
        else:
            message = '{:<10}{:>10}'.format(language_dir[i]+':',file[n])
        surface.append(u.make_font(message))

    choice = 0
    flag = True
    while flag:
        opt_opt = opt_opts(opts[choice])
        opt_choice = opt_opt.index(file[choice])

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    flag = False
                
                if event.key == K_DOWN:
                    if choice+1 < len(opts):
                        choice += 1
                    else:
                        choice = 0
                
                if event.key == K_UP:
                    if choice > 0:
                        choice -= 1
                    else:
                        choice = len(opts)-1
                
                if event.key == K_RIGHT:
                    if opt_choice+1 < len(opt_opt):
                        opt_choice += 1
                    else:
                        opt_choice = 0
                    file[choice]  = opt_opt[opt_choice]
                
                if event.key == K_LEFT:
                    if opt_choice > 0:
                        opt_choice -= 1
                    else:
                        opt_choice = len(opt_opt)-1
                    file[choice]  = opt_opt[opt_choice]
                
                if event.key == K_RETURN:
                    if opts[choice] == 'exit':
                        flag = False

        screen.fill((255,255,255))
        for n,i in enumerate(surface):
            width = screen_size[0]//2-i.get_width()//2
            height = screen_size[1]//step + n*(screen_size[1]//step)
            dest = (width,height)
            screen.blit(i,dest)
        
        for n,i in enumerate(opts):
            if i == 'exit':
                message = '{:<10}{:>10}'.format(language_dir[i],file[n])
            else:
                message = '{:<10}{:>10}'.format(language_dir[i]+':',file[n])
            
            if choice == n:
                surface[n] = u.make_font(message,background=(100,100,100))
            else:
                surface[n] = u.make_font(message)

        pygame.display.update()
    
    write_file(file)

if __name__ == '__main__':
    screen_size = r.screen_size()
    mode = r.full_screen()
    screen = u.init_pygame(screen_size,mode)
    main(screen)