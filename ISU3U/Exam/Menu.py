import Circle_Maker , Getting_Old , Lots_O_Numbers , Coin_Toss , List_Hard , os

menu = ('Programming Skill Menu',
    '',
    'A...Task One Hard',
    'B...Task Two Hard',
    'C...Task Three Hard',
    'D...Task Four Hard',
    'E...Task Five Hard',
    '',
    'X...Exit')

choice = ''
while choice != 'X':
    os.system('cls')
    for n in menu:
        print(n)

    print()
    choice = ''
    while len(choice) != 1:
        choice = input('What is your choice? ').upper()
    
    os.system('cls')
    if choice == 'A':
        Circle_Maker.main()
    if choice == 'B':
        Getting_Old.main()
    if choice == 'C':
        Lots_O_Numbers.main()
    if choice == 'D':
        List_Hard.main()
    if choice == 'E':
        Coin_Toss.main()
    print()
    input('Press enter to do back to menu')
