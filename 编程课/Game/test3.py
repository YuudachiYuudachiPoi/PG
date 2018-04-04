import pygame,time
from pygame.locals import *

screen = pygame.display.set_mode((640,480),0,32)

my_rect1 = (100, 100, 200, 150)
my_rect2 = ((100, 100), (200, 150))
#上两种为基础方法，表示的矩形也是一样的
my_rect3 = Rect(100, 100, 200, 150)
my_rect4 = Rect((100, 100), (200, 150))

time.sleep(10)