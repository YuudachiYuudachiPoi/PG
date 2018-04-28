import random

x=0

ll = {}
for n in range(-10,10):
    ll[n] = 0

for n in range(10000000):
    num = random.randint(-10,10)
    print(num)
    x+=num
    if num in ll:
        ll[num] += 1
print(x)
print(ll)