import random

comput_num = random.randint(1,100)
you_num = 0
while you_num != comput_num:
    you_num = input('What is your guess number?(1-100) ')
    if not you_num.isdigit():
        you_num = 0
        print('Your number have to be interger!\n')
        continue
    else:
        you_num = int(you_num)

    if you_num>100 or you_num<0:
        print('Your number have to be between 1 and 100!\n')
        continue

    if comput_num > you_num:
        print('Too Low.\n')

    if comput_num < you_num:
        print('Too Hight.\n')

print('You got it!')

  
