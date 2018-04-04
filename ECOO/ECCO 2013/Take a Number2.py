f = open('DATA11.txt','r')
all = f.read()
data = all.split('\r\n')
f.close
num = int(data[0])
take = 0
serve = 0
for n in range(1,len(data)):
	if data[n]=='TAKE':
	  num += 1
	  if num == 1000:
	    num = 0
	  take += 1
	if data[n]=='SERVE':
	  serve += 1
	if data[n]=='CLOSE':
	  print '%.0f '%take + '%.0f '%(take-serve) + '%.0f'%num
	  take = 0
	  serve = 0
	if data[n]=='EOF':
		break
