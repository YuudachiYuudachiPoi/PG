a = ''
b = ''
c =''

while not a.isdigit():
    a = input('What is the a of ax^2+bx+c=0? ')
a=int(a)

while not b.isdigit():
    b = input('What is the b of ax^2+bx+c=0? ')
b=int(b)

while not c.isdigit():
    c = input('What is the c of ax^2+bx+c=0? ')
c=int(c)

d= b**2+4*a*c

if d < 0:
    print('the roots are not real')
if d == 0:
    print('The roots are two, equal real roots')
if d > 0:
    print('The roots are two, unequal, real roots')