def main():
    import os

    print('List_Hard')
    menu = ('{:>30}'.format('Shark Regatta'),
        '1...add a boat to list',
        '2...remove a boat from lit',
        '3...print a list of boats by sign up order',
        '4...print a list of boats sorted alphabetically',
        '5...print a list of boats sorted alphabetivally and numbered',
        '6...how many boats are in the regatta',
        '9...exit',
        '')
    
    boat_list = []

    choice = 0
    while choice != 9:
        os.system('cls')
        for n in menu:
            print(n)

        go = True
        while go:
            try:
                choice = int(input('What is your choice? '))
            except:
                pass
            else:
                if choice in range(1,7) or choice == 9:
                    go = False

        print()

        if choice == 1:
            go_in = ''
            while len(go_in) == 0:
                go_in = input('What is the name of the boat? ').title()
            try:
                boat_list.append(go_in)
            except:
                print('Error')
            else:
                print(go_in,'has been added to the list.')
        
        if choice == 2:
            r = ''
            while len(r) == 0:
                r = input('What is the name of the boat? ').title()

            try:
                boat_list.remove(r)
            except:
                print(r,'not in the list')
            else:
                print(r,'has been remove from the list ')

        if choice == 3:
            print('List of Boats')
            print()
            for n in boat_list:
                print(n)

        if choice == 4:
            sorted_boat_list = boat_list.copy()
            sorted_boat_list.sort()
            print('Sorted Boats')
            print()
            for n in sorted_boat_list:
                print(n)
        
        if choice == 5:
            sorted_boat_list = boat_list.copy()
            sorted_boat_list.sort()
            print('Sorted and Numbered Boats')
            print()
            for n,k in enumerate(sorted_boat_list):
                print('{:<30}'.format(k),n+1)

        if choice == 6:
            print(len(boat_list))
        print()
        input('Pree enter to fo back to menu.')

main()