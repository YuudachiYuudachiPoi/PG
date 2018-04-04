f = open('C:\DATA40.txt','r')
all = f.read()
data = all.split('\n')
f.close

for time in range(0,5):
	prices =[]
	coupon =[]
	Fprices = 0.0
	for n in range(1,int(data[0])+1):
		prices.append(float(data[n]))
	data = data[n+1:]
	for n in range(1,int(data[0])+1):
		coupon.append(data[n])
	data = data[n+1:]
	prices.sort()
	
#	Dprices=[]
#	for n in range(0,len(prices)-1):
#		Dprices.append(prices[n+1]-prices[n])
#	DPmax = sorted(Dprices)[len(Dprices)-1]
	for 
		Tprices=prices
		while Tprices != []
			