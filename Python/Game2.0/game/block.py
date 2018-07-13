# -*- coding: utf-8 -*-

import read_setting as r
import utill as u
import pygame,sys,os
from pygame import *


def block_menu(screen):
    screen_size = r.screen_size()
    language_dir = r.language()
    opts = ('old','new','exit')
    step = len(opts) + 1
    surface = []
    for n in opts:
        surface.append(u.make_font(language_dir[n]))

    y = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()
                if event.key == K_DOWN:
                    if y+1 < len(opts):
                        y += 1
                    else:
                        y = 0
                if event.key == K_UP:
                    if y > 0:
                        y -= 1
                    else:
                        y = len(opts)-1
                if event.key == K_RETURN:
                    if opts[y] == 'old':
                        read_block(screen)
                    if opts[y] == 'new':
                        make_block(screen)
                    if opts[y] == 'exit':
                        sys.exit()

        screen.fill((255,255,255))
        for n,i in enumerate(surface):
            width = screen_size[0]//2-i.get_width()//2
            height = screen_size[1]//step + n*(screen_size[1]//step)
            dest = (width,height)
            screen.blit(i,dest)
        
        
        for n,i in enumerate(opts):
            if y == n:
                surface[n] = u.make_font(language_dir[i],background=(100,100,100))
            else:
                surface[n] = u.make_font(language_dir[i])

        pygame.display.update()

def all_txt_files(file_dir):
    txt_files = []
    for root,dirs,files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.txt':
                file = os.path.splitext(file)[0]

                txt_files.append(file)
                #txt_files.append('{:<25}'.format(file))
    
    return txt_files


def read_block(screen):
    
    screen_size = r.screen_size()
    pwd = os.path.realpath(__file__)
    path_game = os.path.abspath(os.path.dirname(pwd)+os.path.sep+"..")
    path_block = path_game + '/data/block'
    files = all_txt_files(path_block)
    opts = ['default'] + files

    files = [[]]
    surface = [[]]
    k = 0
    g = 0
    for n,i in enumerate(opts):
        if k == 20:
            k = 0
            files.append([])
            surface.append([])
            g += 1
        files[g].append(i)

        if len(i) > 20:
            message = i[:16]
            message += '...'
        else:
            message = i
        message = '{:<20}'.format(message)
        surface[g].append(u.make_font(message,background=None,color=(0,0,0),antialias=True,size=20))
        k += 1

    y = 0
    x = 0
    
    last_y = 0
    last_x = 0

    flag = True
    while flag:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    flag = False
                    break
                if event.key == K_DOWN:
                    if y+1 < len(files[x]):
                        y += 1
                    else:
                        y = 0
                    break

                if event.key == K_UP:
                    if y > 0:
                        y -= 1
                    else:
                        y = len(files[x])-1
                    break

                if event.key == K_RIGHT:
                    if x+1 < len(files):
                        x += 1
                    else:
                        x = 0
                    
                    try:
                        files[x][y]
                    except:
                        y = len(files[x]) - 1
                    
                    break

                if event.key == K_LEFT:
                    if x > 0:
                        x -= 1
                    else:
                        x = len(files) - 1
                    
                    try:
                        files[x][y]
                    except:
                        y = len(files[x]) - 1
                    break

                if event.key == K_RETURN:
                    file = files[x][y]
                        

        screen.fill((255,255,255))

        width = 0
        height = 0
        for g in surface:
            for k in g:
                dest = (width,height)
                screen.blit(k,dest)
                height += k.get_height()
            height = 0
            width += k.get_width()
        
        for g,i in enumerate(surface):
            for k,n in enumerate(i):
                if last_y == k and last_x == g:
                    name = files[g][k]
                    if len(name) > 20:
                        message = name[:16]
                        message += '...'
                    else:
                        message = name
                    message = '{:<20}'.format(message)
                    surface[g][k] = u.make_font(message,background=None,color=(0,0,0),antialias=True,size=20)
                if y == k and x == g:
                    name = files[g][k]
                    if len(name) > 20:
                        message = name[:16]
                        message += '...'
                    else:
                        message = name
                    message = '{:<20}'.format(message)
                    surface[g][k] = u.make_font(message,background=(100,100,100),color=(0,0,0),antialias=True,size=20)
        last_y,last_x = y,x

        pygame.display.update()
def make_block():
    pass


if __name__ == '__main__':
    screen_size = r.screen_size()
    mode = r.full_screen()
    screen = u.init_pygame(screen_size,mode)
    block_menu(screen)