# -*- coding: utf-8 -*-
import sys, os
 
try:
    libdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'game')
    sys.path.insert(0, libdir)
except:
    # in py2exe, __file__ is gone...
    pass
 
import menu as m
import utill as u
import read_setting as r

screen_size = r.screen_size()
mode = r.full_screen()
screen = u.init_pygame(screen_size,mode)
m.main(screen)