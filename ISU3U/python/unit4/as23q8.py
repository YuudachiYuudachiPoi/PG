num = int(input('Puck a number. '))

while num not in range(1,5):
    print('Sorry that is wrong.')
    num = int(input('Try again. What is your guess? '))
else:
    print('Good guess, You got it.')