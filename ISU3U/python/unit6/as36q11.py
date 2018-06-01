print('{:<20}{}'.format('Student','Rank'))
s_r = {'Bob':5,'Sue':4,'Jorge':3,'Antoine':2,'Rajeev':1}

for name in s_r:
    mass = '{:<20}{}'.format(name,s_r[name])
    print(mass)