names = []

enter = True
while enter:
    name = input('neter the player in Volleybal Team ')

    if name == 'eop':
        enter = False
    else:
        names.append(name)

print()
names.sort
for k in names:
    print(k)