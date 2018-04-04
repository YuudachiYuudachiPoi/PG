f= open('E:\PG\DATA22.txt','r')
data = f.read().split('\n')
f.close

for n in range(0,10):
	h = int(data[0])
	num = data[1:h+1]
	for p in range(0,h+1):
		data.pop(0)
	tnum=[]
	for id in num:
		id = id.split(' ')
		id.pop(0)
		for a in range(0,len(id)):
			if id[a].isdigit():
				tnum.append(int(id[a]))
	minnum=sorted(tnum)[0]
	#print(minnum,' ',sorted(tnum))
	xx = []
	for id in num:
		id = id.split(' ')
		hh = int(id[0])
		id.pop(0)
		for gg in id:
			if int(gg)==minnum:
				xx.append(hh)
				break
		xx = sorted(xx)
		nxx =[]
		for jj in xx:
			jj = str(jj)
			nxx.append(jj)
	rr = '{'+','.join(nxx)+'}'
	print(minnum,rr)