a = [10,34,42,46,58,90,154,262]

while True:

    for n in a[1:]:
        if a[0] != n:
            break
    else:
        break


    b = []
    for n,k in enumerate(a[:-1]):
        b.append(k-a[n+1])
    print(b)
    a = b