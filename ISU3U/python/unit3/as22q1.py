name = input('What is your name? ')

age = ''
while not age.isdigit():
    age = input('How old are you? ')
age = int(age)

if age > 16:
    job = ''
    while not(job == 'work' or job == 'school'):
        job = input('Do you work or to go school? ').lower()

    if job == 'work':
        work_place = input('Where do you work? ')

        work_time = ''
        while not work_time.isdigit():
            work_time = input('How long have you worked there?(in year) ')
        work_time = int(work_time)

        work_like = ''
        while not (work_like == 'yes' or work_like == 'no'):
            work_like = input('Do you like your job? ').lower()

        if work_like == 'yes':
            work_like = 'You like your job.'
        elif work_like == 'no':
            work_like = 'But you do not like your job.'

        print('\nYour name is',name+'.','\n'+
            'You are working in',work_place+'.','\n'+
            'You worked there for',work_time,'year.',
            work_like
            )

    elif job == 'school':
        school = ''
        while school == '':
            school = input('Which school you are going?(NCC, Quinte Christian or Other) ').lower()

        best_subject = ''
        while best_subject == '':
            best_subject = input('What is your best subject?(Computer, Math or Other) ').lower()
        
        if school == 'ncc':
            print('You are in NCC! me, too.')
        elif school == 'quinte christian' or school == 'quinte':
            print('Oh, you are in Quinte Christian. I haer it before.')
        else:
            print('I never hear it before.')

        if best_subject == 'computer':
            print('me, too. I like computer.')
        elif best_subject == 'math':
            print('ME,too. I like math!')
        else:
            print('oh, go away!')

elif age < 14:
    music_like = ''
    while not(music_like == 'yes' or music_like == 'no'):
        music_like = input('Do you like music? ').lower()
    
    if music_like == 'yes':
        music_type = input('Waht type?(Rock, Country otr other) ').lower()
        print("I don't know much about music. I don't know what is it. ")

    elif music_like == 'no':
        print('Ok. I see.')
    
