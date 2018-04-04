a = open("E:\PG\DATA10.txt","r")
all = a.readlines()
for n in range(0,len(all)):
	cl = all[n]
	data = cl.split()
	D = int (data[0])-1
	H = int (data[1])
	M = int (data[2])
	
	S = D*24*60*60 + H *60*60 + M*60
	OMD = 24*60*60 + 37*60 + 22
	OMH = OMD/24
	OMM = OMH/60
	MD = (S//OMD)+1
	S -= (MD)*OMD
	MH = S//OMH
	S -= MH*OMH
	MM = S//OMM
	
	MD = "%.0f"%(MD+1)
	MH = "%.0f"%MH
	MM = "%.0f"%MM
	
	if len(MH)==1:
		MH = "0"+MH
	if len(MM)==1:
		MM = "0"+MM
	print("DAY",MD+",",MH+":"+MM)