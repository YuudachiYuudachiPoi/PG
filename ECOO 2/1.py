f= open('E:\PG\ECOO 2\DATA11.txt','r')
data = f.read().split('\n')
f.close

for loop in range(10):
    first = data[0].split(' ')
    c = int(first[0])
    o = int(first[1])
    w = int(first[2])
    s = int(first[3])

    second = data[1].split(' ')
    third = data[2].split(' ')

    for p in range(3):
        data.pop(0)
    
    for n,k in enumerate(second):
        second[n] = int(k)
    
    for n,k in enumerate(third):
        third[n] = int(k)

    mix_o = 0
    while True:
        while c-second[0]>=0 and w-second[1]>=0: 
            c -= second[0]
            w -= second[1]
            s += second[2]
            o += second[3]

        if o > mix_o:
            mix_o = o

        while s-third[0]>=0 and o-third[1]>=0: 
            s -= third[0]
            o -= third[1]
            c += third[2]
            w += third[3]
        if (c-second[0]<0 or w-second[1]<0) and (s-third[0]<0 or o-third[1]<0):
            break
    print(mix_o)