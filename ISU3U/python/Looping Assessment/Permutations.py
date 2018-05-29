def main():
    N=int(input('How many objects? '))
    R=int(input('How many places? '))
    Nc=N
    Np=1
    while Nc >= 1:
        Np=Np*Nc
        Nc=Nc-1
    P=N-R
    Pc=P
    Pp=1
    while Pc >= 1:
        Pp=Pp*Pc
        Pc=Pc-1
    print('Total permutations:',Np)
    A=(Np)/(Pp)
    print("Permutations taken",R,"each time:",A)