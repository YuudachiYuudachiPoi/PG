f = open('people list.txt','r')
data = f.read().split('\n')
f.close

people = {}
for n in data:
    aaa = n.split(' ')
    name = aaa[0]
    table = int(aaa[1])
    people[name] = table

#---------------
import tkinter as tk
window = tk.Tk()

window.title('My windows')
window.geometry('1920x1080')



help = tk.Label(window,
    text='Press tap in your name.',
    bg='white',
    font=('Arial',12),
    width=20,height=2
    )

def search_people():
    pass

search = tk.Button(window,
    text='search',
    width=10,height=2,
    command = search_people
    )

go_back = tk.Button(window,
    text='go back',
    font=('Arical',12),
    width=15,height=2
    )



help.pack()
search.pack()




window.mainloop()