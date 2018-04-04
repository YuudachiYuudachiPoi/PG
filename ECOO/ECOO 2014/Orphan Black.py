f = open("C:\\Users\mcgog\OneDrive\文档\编程\ECOO 2014\DATA20.txt","r")
data = f.read().split('\n')
for time in range (0,len(data)//2):
	c1 =False
	c0 =False
	cc1 = False
	cc0 = False
	dna = data[0+time*2]
	print(dna)
	cg1at0 = dna.replace('C','1').replace('G','1').replace('A','0').replace('T','0')
	cg0at1 = dna.replace('C','0').replace('G','0').replace('A','1').replace('T','1')
	for n in range(0,8):
		for k in range(0,len(dna)//8):
			cn1 = int(cg1at0[n+k*8:n+k*8+8],2)
			if (cn1>=65 and cn1<=90) or cn1==32:
				c1 = True
			else:
				c1 = False
			if not c1:
				break
		else:
			cc1 = True
			break
		for k in range(0,len(dna)//8):	
			cn0 = int(cg0at1[n+k*8:n+k*8+8],2)
			if (cn0>=65 and cn0<=90) or cn0==32:
				c0 = True
			else:
				c0 = False
			if not c0:
				break
		else:
			cc0 = True
			break
	print(cc1,cc0)
	if cc1:
		true_n = cg1at0[n:len(cg1at0)]
		print('c1',cg1at0)
	if cc0:
		true_n = cg0at1[n:len(cg0at1)]
		print('c0',cg0at1)
	print(true_n)
	for n in range(0,len(true_n)//8):
		rn= chr(int(true_n[0+n*8:8+n*8],2))
		print(rn,end='')
	else:
		print()