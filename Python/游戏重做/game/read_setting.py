import os

def read_file():
    pwd = os.path.realpath(__file__)
    path_game = os.path.abspath(os.path.dirname(pwd)+os.path.sep+"..")
    f = open(path_game+'\data\setting.txt','r')
    data = f.readlines()
    f.close
    for n,a in enumerate(data):
        data[n] = a.split(' ')[0]

    return data

def language():
    language = read_file()[0]
    language_dir = {}
    if language == 'English':
        language_dir['start'] = 'start'
        language_dir['setting'] = 'setting'
        language_dir['exit'] = 'exit'
    elif language == 'Chinese':
        language_dir['start'] = '开始'
        language_dir['setting'] = '设置'
        language_dir['exit'] = '离开'

    return language_dir
        
def screen_size():
    screen = read_file()[1].split(',')
    size1 = int(screen[0])
    size2 = int(screen[1])
    
    return (size1,size2)

if __name__ == '__main__':
    print(read_file())
