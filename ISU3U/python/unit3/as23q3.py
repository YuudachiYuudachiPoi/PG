num = []
for n in range(4):
    inpu = int(input('What is thr No.'+str(n+1)+' number. '))
    num.append(inpu)

num = sorted(num)
print(num)