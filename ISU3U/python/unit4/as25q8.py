for n in range(10):
    out = ''
    if n==0:
        out+='. '*4+'.'
    else:
        out+=' '*4+'.'+' '*4

    
    out += ' '*(3+n)+'.'+' '*(8-n)
    

    print(out)