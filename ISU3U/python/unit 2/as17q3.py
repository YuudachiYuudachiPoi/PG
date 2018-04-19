money = ''
while not money.isdigit():
    money = input('How many money yo have?')
money = int(money)
if money < 10000:
    print('less than $1000 earns 3%.')
elif money < 25000:
    print('4%')
elif money < 50000:
    print('5%')
elif money < 75000:
    print('6%')
else:
    print('7%')