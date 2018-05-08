for n in range(10):
    out = ''
    if n==1:
        out+='. '*4+'.'
    else:
        out+=' '*4+'.'+' '*4
    print(out)