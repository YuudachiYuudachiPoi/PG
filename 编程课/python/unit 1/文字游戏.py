sw = 'banana'
gw = '_'*len(sw)

while sw != gw:
    g = ''
    while len(g)!=1:
        g = input('What is your letter?')

    for n in range(len(sw)):
        if g == sw[n]:
            gw = gw[0:n]+g+gw[n+1:len(gw)]
    print(gw)
print('Youe get it')