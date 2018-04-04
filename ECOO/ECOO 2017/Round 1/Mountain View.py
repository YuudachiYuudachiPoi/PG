import re
f = open('C:\\Users\XiLI\OneDrive\文档\编程\ECOO\ECOO 2017\Round 1\DATA\DATA31.txt','r')
data = f.read().split('\n')
for loop_time in range(0,3):
	number_of_mountains = data[0]
	data.pop(0)
	mountains_hight_list = data[0].split(' ')
	data.pop(0)
	
	class mountains(object):
		def __init__(self,right):
			self.__right = right
		def get_right(self):
			return self.__right
		def get_name(self):
			return self.__name
			
	for n in range(0,len(mountains_hight_list)-1):
		t = 'm'+str(n)+'=mountains('+str(n+1)+')'
		print (t)
		exec(t)
