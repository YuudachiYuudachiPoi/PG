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
                    else:
                        choice = 0
                if event.key == K_UP:
                    if choice > 0:
                        choice -= 1
                    else:
                        choice = len(opts)-1
                if event.key == K_RETURN:
                    if opts[choice] == 'old':
                        read_block(screen)
                    if opts[choice] == 'new':
                        make_block(screen)
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

def all_txt_files(file_dir):
    txt_files = []
    for root,dirs,files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.txt':
                txt_files.append(os.path.splitext(file)[0])
    
    return txt_files


def read_block(screen):
    flag = True
    
    pwd = os.path.realpath(__file__)
    path_game = os.path.abspath(os.path.dirname(pwd)+os.path.sep+"..")
    path_block = path_game + '\data\block'
    files = all_txt_files(path_block)
    opts = ['default'] + files
    choice = 0
    while flag:
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
                

def make_block():
    pass


if __name__ == '__main__':
    screen_size = r.screen_size()
    mode = r.full_screen()
    screen = u.init_pygame(screen_size,mode)
    block_menu(screen)