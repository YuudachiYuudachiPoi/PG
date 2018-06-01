letter =['']

for n in range(65,91):
    letter.append(chr(n))

a = ''
while len(a) != 1:
    a = input('Give me a leter please ')

a = a.upper()
order = letter.index(a)
print(a + ' is leter number %.d in the alphabet'%order)