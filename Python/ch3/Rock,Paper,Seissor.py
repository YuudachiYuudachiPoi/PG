import random
computer_choice = random.chose('rock','paper','scissors')

#if random_choice == 0:
#	computer_choice = 'rock'
#elif random_choice == 1:
#	computer_choice = 'paper'
#else:
#	computer_choice = 'scissors'

print('The computer chooses',computer_choice)

user_choice = input('rock,paper or scissors? ')
print('You chose',user_choice,'and the computer chose', computer_choice)