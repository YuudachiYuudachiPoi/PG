q=0
for x in range(1,100000000):
	n=x
	k=0
	while n != 1:
		k += 1
		if n/2-n//2 != 0:
			n = (3*n+1)/2
		else:
			n = n/2
	print(x,':',k)
	if k>>q:
		y=x
		q=k
print(y,':',q)