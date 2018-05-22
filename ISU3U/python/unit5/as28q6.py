n = int(input('What is N? '))

sum = 0
number = 1
while True:
    sum += number
    number += 1
    if sum == n:
        print('This is a perfect number.')
        break
    elif sum > n:
        print('This is no a perfect number.')
        break