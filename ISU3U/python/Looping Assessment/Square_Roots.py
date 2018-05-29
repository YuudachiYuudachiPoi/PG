def main():
    n = float(input('number? '))
    accuracy = int(input('accuracy?(1-10) '))
    g = n/2

    q = n/g

    while abs(q - g) > 10**(-accuracy-1):
        g = (q+g)/2
        q = n/g
    print('The square root of %.f is'%n,round(g,accuracy))