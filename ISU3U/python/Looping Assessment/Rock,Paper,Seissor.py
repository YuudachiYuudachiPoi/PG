import random
money = 25
print('\nYou start with $25.')
print('Every game is worth a $5.\n')

while money >= 5:
    computer_choice = random.choice(('rock','paper','scissors'))

    #if random_choice == 0:
    #	computer_choice = 'rock'
    #elif random_choice == 1:
    #	computer_choice = 'paper'
    #else:
    #	computer_choice = 'scissors'

    #print('The computer chooses',computer_choice)
    user_choice = ''
    while (user_choice != 'rock' and
            user_choice != 'paper' and
            user_choice != 'scissors'):
        user_choice = input('rock, paper or scissors? ').lower()
    money -= 5
    #print('You chose',user_choice,'and the computer chose', computer_choice)
    if user_choice == computer_choice:
        winner = 'Tie'
    elif computer_choice == 'paper' and user_choice == 'rock':
        winner = 'Computer'
    elif computer_choice == 'rock' and user_choice == 'scissors':
        winner = 'Computer'
    elif computer_choice == 'scissors' and user_choice == 'paper':
        winner = 'Computer'
    else:
        winner = 'User'

    if winner == 'Tie':
        print('We both chose',computer_choice + ', you got your $5 back.')
        money += 5
    elif winner == 'Computer':
        print(winner,'won. The computer chose',computer_choice + '.')
    elif winner == 'User':
        print(winner,'won. The computer chose',computer_choice + ', you got $10.')
        money += 10
    print('You have $%.d now'%money)

    quit = ''
    while not(quit == 'yes' or quit == 'no'):
        quit = input('Do you want to quit? ').lower()
        print()

    if quit == 'yes':
        break
else:
    print('You lost all your money')
print('Thank you to play this game')