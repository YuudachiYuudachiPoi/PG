names = []

enter = True
while enter:
    name = input('enter the caoures you are taking, please ')

    if name == 'eoc':
        enter = False
    else:
        names.append(name)

print()
for k in names:
    print(k)