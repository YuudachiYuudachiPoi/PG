f= open('E:\PG\ECOO 2\DATA21.txt','r')
data = f.read().split('\n')
f.close

for loop in range(0,10):
    n = int(data[0])
    work = data[1:n+1]
    for p in range(0,n+1):
        data.pop(0)
    
    d_box={}
    for n in work:
        aa = n.split(' ')
        if not int(aa[0]) in d_box:
            d_box[int(aa[0])] = []
        d_box[int(aa[0])].append(float(aa[1]))

    for key,values in d_box.items():
        d_box[key] = sorted(values)[::-1]

    open_day = 0
    mark = 0
    for day in range(1,1000001):
        if day in d_box:
            for n in range(open_day+1):
                if len(d_box[day]) != 0:
                    mark += d_box[day][0]
                    d_box[day].pop(0)
                    open_day = open_day-n
                else:
                    break
            d_box.pop(day)
        else:
            open_day += 1
        if len(d_box) == 0:
            break
    mark = str('%.4f'%mark)
    print(mark)