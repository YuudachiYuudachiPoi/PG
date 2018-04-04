f = open("E:\PG\DATA31.txt",'r')
data =f.read().split('\n')
f.close
for assdaf in range(0,10):
	fl = data[0].split(' ')
	N = int(fl[0])
	X = int(fl[1])
	Y = int(fl[2])
	Z = int(fl[3])
	hh = data[1:N+1]
	xx = data[N+2:N+2+N]
	fw = []
	for n in range(0,N):
		fw.append('')
	for n in range(0,N+3+N):
		data.pop(0)
	for a in range(0,len(hh)):
		w = hh[a]
		for n in range(0,len(w)):
			num = int(w[n])
			if num ==0:
				kk=Z
			if num//2-num/2==0 and num != 0:
				kk = num+X
			if num//2-num/2!=0 and num != 0:
				kk = num-Y
				if kk<0:
					kk = 0
			fw[a]+=str(kk)
	fail= []
	for qq in range(0,len(fw)):
		if fw[qq]!=xx[qq]:
			fail.append(str(qq+1))
	if len(fail) == 0:
		print('MATCH')
	else:
		print('FAIL: ',end='')
		print(','.join(fail))
			