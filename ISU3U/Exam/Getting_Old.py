def main():
    import time
    print('Getting Old Hard')
    print()

    go = True
    while go:
        try:
            age = int(input('How old you you? '))
        except:
            pass
        else:
            if age >= 0:
                go = False
    
    gender = ''
    while not (gender == 'f' or gender == 'm'):
        gender = input('What is your gender(m/f)? ').lower()
    
    print()
    #------------------------------------------------------------------
    if age in range(0,9):
        name = 'child'
    elif age in range(9,13):
        name = 'tweeny'
    elif age in range(13,20):
        name = 'teenager'
    elif age >=20:
        name = 'old timer'
    
    if gender == 'f':
        print('You are a girl',name+'.')
    elif gender == 'm':
        print('You are a boy',name+'.')
    
    print('You were born in the year %.d.'%(2018-age))

    if age//2 == 0:
        print('You age is an even number.')
    else:
        print('You age is an odd number.')
    
