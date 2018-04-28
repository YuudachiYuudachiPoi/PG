num = ''
while  not num.isdigit():
    num = input('You must neter a num between 1 and 6! ')
    if num.isdigit():
        if int(num) not in range(1,7):
            num = ''
num = int(num)

if num == 1:
    print('Unexpected money will arrive.')
if num == 2:
    print('Happiness is assured.')
if num == 3:
    print('Travel is in the near future.')
if num == 4:
    print('New acquaintance appears fruitful.')
if num == 5:
    print('A promototion is around the corner.')
if num == 6:
    print('A diaster awaits you.')