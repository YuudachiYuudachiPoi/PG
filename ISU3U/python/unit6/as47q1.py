candies = ['mars bar', 'rocket', "o'henry", 'smarties', 'puff banana']

eat_another = True
while eat_another:
    for  candy in candies:
        print(candy)
    print()
    want_eat = ''
    while not want_eat  in candies:
        want_eat = input('Which candy would you like to eat? ')
    candies.remove(want_eat)

    ask = ''
    while not (ask == 'yes' or ask == 'no'):
        ask = input('Would you like to eat another candy? ').lower()
    print()
    
    if ask == 'no':
        eat_another = False
    elif len(candies) == 0:
        eat_another = False