f =open('C:\\Users\mcgog\OneDrive\文档\编程\ECOO 2018\DATA10.txt','r')
data = f.read().split('\n')
for asdfgh in range(0,2):
	fl= data[0].split(' ')
	t = int(fl[0])
	n = int(fl[1])
	day = data[1:n+1]
	for k in range(0,n+1):
		data.pop(0)
	for k in day:
		if k == 'E':	
			day.pop(0)
		if k == 'B':	
			for q in range(0,t):
				day.pop(0)
		print(k,day)