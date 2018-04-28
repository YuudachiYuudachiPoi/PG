num = ''
while not num.isdigit():
    num = input('Please enter s number. ')
    if num.isdigit():
        if int(num) < 0:
            num = ''

print('YOU ANSWERED',num,'QUESTIONS')
