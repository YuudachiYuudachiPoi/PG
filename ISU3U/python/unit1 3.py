import sys,time
k = 0
a= []
for n in range(0,4):
	y= int(input("No.%d number?"%(n+1)))
	if y >= 10:
		print("error:number >= 10")
		sys.exit()
	a.append(y)
	t = time.time()
while a != [6,1,7,4]:
	k+=1
	a = sorted(a)
	s = a[0]*1000+a[1]*100+a[2]*10+a[3]
	l = a[3]*1000+a[2]*100+a[1]*10+a[0]
	p = l-s
	for n in range(0,4-len(str(p))):
		a[n]=0
	for q in range(0,len(str(p))):
		a[n]=int(str(p)[q])
	if (time.time() - t) > 5:
		print("time out: 5s")
		break
print(k,"time(s)")