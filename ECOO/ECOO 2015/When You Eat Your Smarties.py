f= open('C:\DATA10.txt','r')
all= f.read()
data = all.split('\n')
f.close

time=0
Color = {"orange":0,"blue":0,"green":0,"yellow":0,"pink":0,"violet":0,"brown":0,"red":0}
for S in data:
	for C in Color:
		if S == C:
			Color[C]+=1			
for C in Color:
	if C == 'red':
			time += Color[C]*16
	else:
		if Color[C]/7-Color[C]//7 == 0:
			time += (Color[C]//7)*13
		else:
			time += (Color[C]//7+1)*13
print(time)