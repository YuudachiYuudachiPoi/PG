num = [1,1]
k = 1

while 100000>len(num):
    k += 1
    num.append(num[k-1]+num[k-2])

for n in num:
    print(n)