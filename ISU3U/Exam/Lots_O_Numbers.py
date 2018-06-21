def main():
    import time
    print('Lots O Number Hard')
    print()

    go = True
    while go:
        try:
            start = int(input('What number do you want to start at? '))
        except:
            pass
        else:
            go = False
    
    go = True
    while go:
        try:
            end = int(input('What number do you want to end at? '))
        except:
            pass
        else:
            go = False
    
    want = ''
    while not (want == 'u' or want == 'd'):
        want = input('Do you want to go up or down(u/d)? ').lower()
    
    if want == 'u':
        question = 'What do you want to go up by? '
    elif want == 'd' :
        question = 'What do you want to go down by? '
    go = True
    while go:
        try:
            number_go = int(input(question))
        except:
            pass
        else:
            if number_go > 0:
                go = False
    
    print()

    #-------------------------------------------------------------------
    number_list = []

    if want == 'u':
        end += 1
    if want == 'd':
        end -= 1
        number_go = -number_go

    for n in range(start,end,number_go):
        print(n,end=' ')
        time.sleep(1)
    print()
    print()

    #--------------------------------------------------

    print('There are %.d numbers.'%len(number_list))

    sum = 0
    for n in number_list:
        sum += int(n)
    
    print('The sum of your number is %.d.'%sum)

    try:
        average = sum/len(number_list)
        print('The average of your number is %.1f.'%average)
    except:
        print('Error')
