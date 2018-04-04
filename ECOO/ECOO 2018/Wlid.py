f = open('E:\PG\DATA10.txt','r')
data = f.read().split('\n')
for asdf in range(0,2):
	fl = data[0].split(' ')
	T = int(fl[0])
	N = int(fl[1])
	day = data[1:N+1]
	for n in range(0,N+1):
		data.pop(0)
	
	cabter = 0
	for la in day:
		if la == 'B':
			cabter+=1
	print(cabter)