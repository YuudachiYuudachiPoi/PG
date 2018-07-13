# -*- coding: utf-8 -*-

import read_setting as r
import utill as u



def main(screen,ball_speed,table_speed):
    pass
if __name__ == '__main__':
    screen_size = r.screen_size()
    mode = r.full_screen()
    screen = u.init_pygame(screen_size,mode)
    main(screen,)