def main():
    import random
    print('Coin Toos Hard')

    go = True
    while go:
        try:
            number = int(input('How many coins would you like to toss(>0)? '))
        except:
            pass
        else:
            if number > 0 :
                go = False
    
    go = True
    while go:
        try:
            time = int(input('How many times would you like to toss the %.d coins(>0)? '%number))
        except:
            pass
        else:
            if time > 0 :
                go = False
    print()
    #--------------------------------
    for n in range(time):
        for k in range(number):
            print(random.choice(('H','T')))
        print()