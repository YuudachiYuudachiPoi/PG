name = input('What is your name? '
num = ''
while not num.isdigit():
    num = input('How much would you like their yearly salary to be? ')
num = int(num)

if num >=55000:
    print('Take ICS 3U')
elif num >=35000:
    print('Take BTA 3O')
elif:
    print('Take TGJ 3O')
else:
    print('Skip computers')