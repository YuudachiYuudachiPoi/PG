def main():
    print(" YEAR             INTEREST             AMOUNT")
    Y=1626
    A=24.00

    while Y <= 1699:
        I=A*0.02
        A=A+I
        print( Y,"             ",round(I,2),"              ",round(A,2))
        Y=Y+1
    while Y <= 1799:
        I=A*0.03
        A=A+I
        print( Y,"             ",round(I,2),"              ",round(A,2))
        Y=Y+1
    while Y <= 1899:
        I=A*0.04
        A=A+I
        print( Y,"             ",round(I,2),"              ",round(A,2))
        Y=Y+1
    while Y <= 2016:
        I=A*0.05
        A=A+I
        print( Y,"             ",round(I,2),"              ",round(A,2))
        Y=Y+1