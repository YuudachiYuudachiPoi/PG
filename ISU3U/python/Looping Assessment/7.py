square = float(input())

number = square // 2 

g = 100

p = 0

while True:
    change = 1 * 10**p
    print(round(number**2,g))
    if round(number**2,g) == round(square,g):
        print(number)
        break
    elif (number+change)**2 > square and (number-change)**2 < square:
        p -= 1
    elif number**2 < square:
        number += change
    elif number**2 > square:
        number -= change
