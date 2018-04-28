gender = input('What is your gender (m/f)? ')
weight = int(input('What is your weight? '))
height = int(input('What is your height? '))

if gender == 'm':
    if weight < 100:
        if height < 5:
            print('You are a very short, light male.')
        else:
            print('You are a boy who weight at least 100 ppunds.')
    else:
        print('You are a boy who weight at least 100 pounds.')
else:
    if height > 6:
        print('You are a tall girl.')
    elif height > 5:
        print('You are a not so tall girl.')
    else:
        if weight >= 200:
            print('You are a very heavy, short girl.')
        else:
            print('You are a less than 200 pound short female.')
print('Thank you for using my program.')