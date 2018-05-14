num = [1,1]
k = 1

while 20>len(num):
    k += 1
    num.append(num[k-1]+num[k-2])

print(num)