f= open('E:\PG\ECOO 2\DATA2l0.txt','r')
data = f.read().split('\n')
f.close

for loop in range(10):
    num_p = data[0]
    points = []
    data.pop(0)
    x_box=[]

    for n in range(num_p):
        lll = data[n].split(' ')
        x = int(lll[0])
        y = int(lll[1])
        points.append((x,y))
        x_box.append(x)
    
    x_box = sorted(x_box)
    
    sorted_points = []
    for n in x_box:
        for k in points:
            if 
    

