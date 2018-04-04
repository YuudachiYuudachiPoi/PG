f = open('C:\\Users\XiLi\OneDrive\文档\编程\ECOO\ECOO 2017\Round 2\DATA\DATA20.txt','r')
data = f.read().split('\n')
for loop_time in range(2):

	box_size = int(data[0])
	data.pop(0)
	
	box = []
	for y in range(box_size):
		line= []
		for x in range(box_size):
			line.append(data[y][x])
		box.append(line)
	
	for n in range(box_size):
		data.pop(0)
	
	print(box)