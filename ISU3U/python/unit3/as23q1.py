number1 = int(input('What is your number? '))
number2 = int(input('What is your number? '))
number3 = int(input('What is your number? '))

if number1 >= number2 and number1 >= number3:
    biggest = number1
    if number2 >= number3:
        second = number2
        last = number3
    else:
        second = number3
        last = number2


elif number2 >= number1 and number2 >= number3:
    biggest = number2
    if number1 >= number3:
        second = number1
        last = number3
    else:
        second = number3
        last = number1

elif number3 >= number1 and number3 >= number2:
    biggest = number3
    if number1 >= number2:
        second = number1
        last = number2
    else:
        second = number2
        last = number1

print(biggest,second,last)