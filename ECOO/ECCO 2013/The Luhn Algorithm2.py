f = open('DATA22.txt','r')
all = f.read()
f.close
data = all.split('\r\n')

for x in range(0,5):
  mdzz = data[x].split(' ')
  for n in range(0,5):
    mmp = 0
    cnm = mdzz[n][::-1]
    #print cnm
    for k in range(0,len(cnm)):
    	if float(k)/2 - k/2 != 0:
    	  mmp += int(cnm[k])
    	else:
    	  haha = str(int(cnm[k])*2)
    	  #print haha
    	  if len(haha)==2:
    	  	mmp += int(haha[0])+ int(haha[1])
    	  else:
    	  	mmp += int(haha)
    mmp = 10-int(str(mmp)[-1])
    #print mmp
    mmp = int(str(mmp)[-1])
    print '\b%.0f'%mmp,
  print
