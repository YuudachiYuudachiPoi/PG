import random
money = 25
print('You start with $25\n')
print('Every game is worth a $5')

while money >= 5 :
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
        print('We both chose',computer_choice + ', play again.')
    elif winner == 'Computer':
        print(winner,'won. The computer chose',computer_choice + ', you lost $5.')
    elif winner == 'User':
        print(winner,'won. The computer chose',computer_choice + ', you got $5.')
        money += 10
    print('You have $%.d\n'%money)
print('You lost all tour money')