import time,os

partiers = []
time_list = {}

def get_time():
    t= time.localtime()
    now = time.asctime(t)
    return now

def add(provide_name):
    global partiers,time_list
    provide_name = provide_name.title()
    if provide_name in partiers:
        print(provide_name, 'alreay signed up. ')
    else:
        partiers.append(provide_name)
        time_list[provide_name] = get_time()
        print(provide_name,'signed up. ')

def remove(provide_name):
    global partiers,time_list
    if provide_name in partiers:
        partiers.remove(provide_name)
        time_list.pop(provide_name)
        print('remove succesful.\n')
    else:
        print(provide_name + ' not in the list. ')

def how_many():
    global partiers
    print(len(partiers))

def sign_up_time(provide_name):
    global time_list
    if provide_name in time_list:
        print(provide_name, 'signed up at', time_list[provide_name])
    else:
        print(provide_name + ' not in the list. ')

def order(provide_number):
    global partiers
    try:
        partier_nmae = partiers[provide_number-1]
    except:
        print('You number is unacceptable. ')
    else:
        print('partirer',provide_number,'is',partier_nmae+'. ')

def last_one():
    global partiers
    print(partiers[-1],'is the last one')

def see_if(provide_name):
    global partiers
    if provide_name in partiers:
        print(provide_name, 'is in the list. ')
    else:
        print(provide_name,'is not in the list. ')

def replace_someone(provide_name_1,provide_name_2):
    global partiers,time_list

    if provide_name_1 in partiers and not provide_name_2 in partiers:
        partiers.remove(provide_name_1)
        time_list.pop(provide_name_1)
        print('remove succesful.\n')

        partiers.append(provide_name)
        time_list[provide_name] = get_time()  
    elif provide_name_2 in partiers:
        print(provide_name, 'alreay signed up ')
    elif  not provide_name_1 in partiers:
        print(provide_name + ' not in the list. ')
    else:
        print('ERROR:replace_someone ')

def print_name():
    global partiers
    for partier in partiers:
        print(partier)

def print_name_with_number():
    global partiers
    for n,partier in enumerate(partiers):
        print('{:<10}'.format(partier),n+1)

def print_name_in_alalphabetically():
    global partiers
    sorted_partiers = partiers.copy()
    sorted_partiers.sort()

    for partier in sorted_partiers:
        print(partier)

def print_name_in_reverse_alalphabetically():
    global partiers
    sorted_partiers = partiers.copy()
    sorted_partiers.sort()
    sorted_partiers = sorted_partiers[::-1]

    for partier in sorted_partiers:
        print(partier)

def party_limit(number):
    global partiers,time_list

    out_list = partiers[:-number]
    partiers = partiers[-number:]
    for out in out_list:
        time_list.pop(out)

def ask_name(question):
    name = input(question)
    while len(name) == 0:
        print('You did no enter anything.try angin ')
        name = input(question)
    return name

menu = ['{:>30}'.format('Menu'),
        '1...add a partier to the list (provide namae) ',
        '2...remove a partier from the list (provide name) ',
        '3...how many a partier from the list? ',
        '4...when did a certain partier to sign up? (provide name) ',
        '5...who was partier 1, 2, 3, etc? (provide name) ',
        '6...who was the last partier to sign up? ',
        '7...see if someone is someone is coming to the party (provide name) ',
        '8...replace on partier with another partier (provide 2 names)',
        '9...print a list of partiers ',
        '10..print a list of partiers with their sign up number ',
        '11..print a list of the partiers sorted alphabetically ',
        '12..print a list of the partier in reverse alphabetical order ',
        '13..set a party limit and pop off the partiers above ',
        '99..exit'
]



def main():
    global menu
    for k in menu:
        print(k)
    print()

    chioce = 0
    while not( chioce in range(1,len(menu)-1) or chioce == 99 ):
        anwer = input('What is your chioce? ')
        while not anwer.isdigit():
            anwer = input("your input isn't a number, What is your chioce? ")
        chioce =int(anwer)
        print()

    if chioce == 99:
        exit = True
    else:
        exit = False
    
        if chioce == 1:
            name = ask_name('Who you want to add? ')
            add(name)
        elif chioce == 2:
            name = ask_name('Who you want to remove? ')
            remove(name)
        elif chioce == 3:
            how_many()
        elif chioce == 4:
            name = ask_name('Which people you want to know? ')
            sign_up_time(name)
        elif chioce == 5:
            number = 0
            while not number > 0:
                anwer = input('What is the provide number? ')
                while not anwer.isdigit():
                    anwer = input("your input isn't a number, What is the procide number")
                number = int(anwer)    
            order(number)
        elif chioce == 6:
            last_one()
        elif chioce == 7:
            name = ask_name('Which one you want to find? ')
            see_if(name) 
        elif chioce == 8:
            name_1 = ask_name('Who you want to remove? ')
            name_2 = ask_name('Who you want to add? ')
            replace_someone(name_1,name_2)
        elif chioce == 9:
            print_name()
        elif chioce == 10:
            print_name_with_number()
        elif chioce == 11:
            print_name_in_alalphabetically()
        elif chioce == 12:
            print_name_in_reverse_alalphabetically()
        elif chioce == 13:
            limit = 0
            while not limit > 0:
                anwer = input('What is the limit? ')
                while not anwer.isdigit():
                    anwer = input("your input isn't a number, What is the limit")
                limit =int(anwer)
            party_limit(limit)
    
    return exit

import os

os.system('cls')
exit = False
while not exit:
    exit = main()
    input()
    os.system('cls')