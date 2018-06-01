dogs = ['border collie', 'australian cattle dog','labrador retriever']

name = input('What is your favourite type of dog? ')

number = ''
while not number in ('0','1','2'):
    number = input('pick a number between 0 and 2 ')
number = int(number)
dogs[number] = name

print(dogs)