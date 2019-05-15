#!/usr/bin/env python
# coding=UTF-8
'''
Author: Howie Hong(希理)
Date: 2019-05-14 20:32:36
LastEditors: Howie Hong(希理)
LastEditTime: 2019-05-14 22:19:05
Description: 
'''

def ask_a_num(question,min,mix,down_message='数字过小',up_message='数字过大'):
    while True:
        answer = input(question)
        if answer.isdigit:
            answer = int(answer)
            if min != None:
                if answer<min:
                    print(down_message,end='')
                    input('按enter继续')
                    continue
            elif max != None:
                if answer>max:
                    print(up_message,end='')
                    input('按enter继续')
                    continue
            return answer
        else:
            print('请输入一个数字')

class FileName():
    import calendar
    year = None
    month = None
    day = None
    file_name = ''

    def ask_date(self):
        while True:
            self.year = ask_a_num('照片拍摄的年份是？',1900,3000,'年份低于1900年，请重新输入','年份大于3000年请重新输入')
            self.month = ask_a_num('照片拍摄的月份是？',1,12) 
            month_range = calendar.monthrange(self.year,self.month)[1]
            self.day = ask_a_num('照片拍摄的日份是？',1,month_range,'数字过小','数字过大，这个月有{}天'.format(month_range))
    def __str__(self):
        return self.file_name

class File():
    import os,sys,time

    file_name = FileName()
    

    def change_path(self,path):
        self.path = path
    def create_file(self):
        path += '\\' + self.file_name
        if  os.path.exists(path):
            print('文件夹已存在')
        else:
            os.makedirs(path)
            print(self.file_name+' 创建成功')


if __name__ == "__main__":
    import sys
    
    print('欢迎使用家庭相册起名软件')
    print()
    file = File()

    while True:
        answer = ask_a_num('''你要把图片在哪个文件下？(输入数字，并按下enter)
        1 - 软件所在目录(家庭相册)(全家的照片)
        2 - 希理的照片
        3 - Daisy的照片
        4 - 爸爸的照片
        0 - 退出
        ''',0,4)
        path = sys.path[0]
        if answer == 1:
            pass
        elif answer == 2:
            path += '\\希理的图片'
        elif answer == 3:
            path += '\\Daisy的图片'
        elif answer == 4:
            path += '\\爸爸的图片'
        else:
            break

        file.change_path(path)
        
        while True:
            answer = ask_a_num('''创建文件夹(输入数字，并按下enter)
                1 - 只创建文件夹
                2 - 创建文件夹并自动把“待整理图片”文件夹中的图片放入新建文件夹中(推荐)
                0 - 返回
                ''',0,2)
