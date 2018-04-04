import re
f = open('DATA30.txt','r')
all = f.read()
data = all.split('\r\n')
f.close
find = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
for num in range(0,3):
	dp=0
	for x in range(num*16,num*16+16):
		for y in range(0,16):
			box = []
			right = []
			if data[x][y] == '-':
				heng = re.findall('\w',data[x])
			#print heng
				for n in range(0,len(heng)):
					box.append(heng[n])
				for n in range(x//16 *16,x//16 *16 +16):
					if data[n][y] == '-':
						continue
					else:
						box.append(data[n][y])
				for n in range((x//4)*4,(x//4)*4 +4):
					for k in range((y//4)*4,(y//4)*4 +4):
						if data[n][k] == '-':
							continue
						else:
							box.append(data[n][k])
			#print box
				for n in range(0,len(find)):  
					if find[n] not in box:
						right.append(find[n])
				if len(right)>0:
					t = list(data[x])
					t[y] = right[0]
					data[x]= ''.join(t)
					#print data[x]
					dp+=1
	print dp
