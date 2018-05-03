import math

num = math.factorial(1000)
k = 5
n=0
while n*k<=num:
    if n*k == num:
        break
    n+=1
print(k)