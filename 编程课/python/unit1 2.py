z = input("What is your number?")
x= z
while len(x)==1:
	y=0
	for n in range(0,len(x)-1):
		y+=int(x[n])
	x = str(y)
if int(x)/3 == int(x)//3:
	print(z,"is a divisible by 3")
else:
	print(z, "is a divisible by 3")
	