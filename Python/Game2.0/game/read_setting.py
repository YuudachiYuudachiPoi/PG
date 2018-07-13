# -*- coding: utf-8 -*-
import os,pygame

def read_file():
    pwd = os.path.realpath(__file__)
    path_game = os.path.abspath(os.path.dirname(pwd)+os.path.sep+"..")
    f = open(path_game+'\data\setting.txt','r')
    data = f.readlines()
    f.close
    for n,a in enumerate(data):
        data[n] = a.split(' ')[0]

    return data

def language():
    language = read_file()[0]
    if language == 'English':
        language_dir = {'start':'start',
                        'setting':'setting',
                        'exit':'exit',
                        'language':'language',
                        'resolution':'resolution',
                        'full screen':'full screen',
                        'old':'use old block file',
                        'new':'create new block file'}
    elif language == 'Chinese':
        language_dir = {'start':'开始',
                        'setting':'设置',
                        'exit':'离开',
                        'language':'语言',
                        'resolution':'分辨率',
                        'full screen':'全屏',
                        'old':'使用旧的方块文件',
                        'new':'制作一个新的方块文件'}

    return language_dir
        
def screen_size():
    screen = read_file()[1].split(',')
    size1 = int(screen[0])
    size2 = int(screen[1])

    return (size1,size2)

def full_screen():
    full_screen = read_file()[2]
    if full_screen == 'Enable':
        mode = pygame.FULLSCREEN
    elif full_screen == 'Disable':
        mode = 0
    
    return mode


if __name__ == '__main__':
    print(read_file())
