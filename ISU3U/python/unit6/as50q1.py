import time

menu = ['{:>10}'.format('Menu'),
        'add a partier to the list (provide namae) ',
        'remove a partier from the list (provide name) ',
        'how many a partier from the list? ',
        'when did a certain partier to sign up? (provide name) ',
        'who was partier 1, 2, 3, etc? (provide name) ',
        'who was the last partier to sign up? ',
        'see if someone is someone is coming to the party (provide name) ',
        'replace on partier with another partier (provide 2 names)',
        'print s list of partiers ',
        'print a list of partiers with their sign up number '
        'print a list of the partiers sorted alphabetically '
        'print a list of the partier in reverse alphabetical order '
        'set a party limit and pop off the partiers above '
]



partiers = {}

def mian():

def get_time():
    t= time.localtime()
    now = time.asctime(t)
    return now

del add(provide_name):
    global partiers
    partiers[provide_name] = now

def remove(provide_name):
    global partiers
    if provide_name in partiers:
        partiers.remove(provide_name)
        print('remove succesful.\n')
    else:
        print(provide_name+' not in the list. ')

def how_many():
    global partiers
    print(len(partiers))

