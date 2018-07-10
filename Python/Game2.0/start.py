# -*- coding: utf-8 -*-
import sys, os
 
try:
    libdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'game')
    sys.path.insert(0, libdir)
except:
    # in py2exe, __file__ is gone...
    pass
 
import menu
menu.main()