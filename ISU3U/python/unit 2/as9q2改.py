n1 = ''
n2 = ''
while not n1.isdigit() and  not n2.isdigit():
    n1 = input('What is your first natural number? ')
    n2 = input('What is your second natural number? ')

n1 = int(n1)
n2 = int(n2)

print('The first number is',n1)
print('The second number is',n2)

if n2 > n1:
    change = n2
    n2 = n1
    n1 = change

sum = n1+n2

print('The sum of',n1,'and',n2,'is',sum)

product = n1 * n2

print('The product of',n1,'and',n2,'is',product)

difference = n1 - n2
print('Subtacting',n1,'by',n2,'gives',difference)

quotient = n1/n2
print('Diciding',n1,'by',n2,'gives',quotient)

remainder = n1%n2
print('The remain of',n1,'divided by',n2,'is',remainder)

dividend = n1//n2
print('The number of times',n1,'goes evenly into',n2,'is',dividend)