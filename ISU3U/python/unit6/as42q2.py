names = []

enter = True
while enter:
    name = input('enter the caoures you are taking, please ')

    if name == 'eoc':
        enter = False
    else:
        names.append(name)

print()
for k,name in enumerate(names):
    print('The %.d course you signed up for is'%(k+1),name)