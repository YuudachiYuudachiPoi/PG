f =open("E:/PG/DATA12.txt","r")
data = f.read().split('\n')
for n in range(0,10):
	q = data[n].split(' ')
	ed = int(q[0])
	eh = int(q[1])
	em = int(q[2])
	ss = (ed-1)*24*60*60+eh*60*60+em*60

	omd = 24*60*60+37*60+22.663
	omh = omd/24
	omm = omh/60
	
	md = int(ss//omd)
	ss = ss - md*omd
	
	mh = int(ss//omh)
	ss = ss - mh*omh
	
	mm = int(ss//omm)
	
	md = md+1
	
	md = str(md)
	mh = str(mh)
	mm = str(mm)
	if len(mh)==1:
		mh = '0'+mh
	if len(mm)==1:
		mm = '0'+mm
	print("Day "+md+", "+mh+':'+mm)

a = input()