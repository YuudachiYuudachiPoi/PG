f = open('C:\\Users\XiLI\OneDrive\文档\编程\ECOO\ECOO 2017\Round 1\DATA\DATA22.txt','r')
data = f.read().split('\n')
for loop_time in range(0,10):
	number_of_chocolates = int(data[0])
	data.pop(0)
	chocolate_list=[]
	class chocolate(object):
		def __init__(self,name,p,f,g):
			self.p = p
			self.f = f
			self.g = g
			self.name = name
		def get_p(self):
			return self.p
		def get_f(self):
			return self.f
		def get_g(self):
			return self.g
		def get_name(self):
			return self.name
		def get_total(self):
			return self.p + self.f + self.g
		
	for judge_time in range(number_of_chocolates):
		chocolate_list.append('c'+str(judge_time))
		t = chocolate_list[judge_time]+'=chocolate(\''+ data[0] +'\',0,0,0)'
		data.pop(0)
		exec(t)
		
		while True:
			if data[0][0] == 'J':
				exec(chocolate_list[judge_time]+'.get_p += int(data[0][2])')
				exec(chocolate_list[judge_time]+'.get_f += int(data[0][4])')
				exec(chocolate_list[judge_time]+'.get_g += int(data[0][2])')
				