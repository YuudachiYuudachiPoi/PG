n1 = int(input('What is your first natural number? '))
n2 = int(input('What is your second natural number? '))

print('The first number is',n1)
print('The second number is',n2)

sum = n1+n2

print('The sum of',n1,'and',n2,'is',sum)

product = n1 * n2

print('The product of',n1,'and',n2,'is',product)

difference = n1 - n2
if difference<0:
    print('Subtacting',n2,'by',n1,'gives',-difference)
else: 
    print('Subtacting',n1,'by',n2,'gives',difference)

quotient = n1/n2
if quotient<1:
    print('Diciding',n2,'by',n1,'gives',1/quotient)
else: 
    print('Diciding',n1,'by',n2,'gives',quotient)

if quotient<1:
    remainder = n2%n1
    print('The remain of',n2,'divided by',n1,'is',remainder)
else:
    remainder = n1%n2
    print('The remain of',n1,'divided by',n2,'is',remainder)

if quotient<1:
    dividend = n2//n1
    print('The number of times',n2,'goes evenly into',n1,'is',dividend)
else:
    dividend = n1//n2
    print('The number of times',n1,'goes evenly into',n2,'is',dividend)