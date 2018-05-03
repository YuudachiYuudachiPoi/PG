import random

num = str(random.randint(1,100))

guess_num = input('Guess a number(1-100) ' )
time = 1
while guess_num != num:
    if not guess_num.isdigit():
        print('Your number have to be int')
        guess_num = input('Try again. What is your guess?(1-100) ')
    elif int(guess_num)<0 or int(guess_num)>100:
        print('Your number have to be in 1-100')
        guess_num = input('Try again. What is your guess?(1-100) ')
    else:
        time += 1
        guess_num = int(guess_num)
        num = int(num)
        if guess_num < num:
            print('Sorry that is wrong.Highter')
            guess_num = input('Try again. What is your guess?(1-100) ')
        elif guess_num > num:
            print('Sorry that is wrong.Lower')
            guess_num = input('Try again. What is your guess?(1-100) ')
        num = str(num)
        guess_num = str(guess_num)
else:
    print('You got it!')