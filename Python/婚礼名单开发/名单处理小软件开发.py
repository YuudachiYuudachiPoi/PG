data = open('people list.txt','r')








#---------------
import tkinter as tk
window = tk.Tk()

window.title('My windows')
window.geometry('1920x1080')

help = tk.Label(window,
    text='Press tap in your name.',
    bg='white',
    font=('Arial',12),
    width=15,height=2
    )

search = tk.Botton(window,
    text='search',
    width=15,height=2,
    command = search_people
    )

help.pack()
search.pack()

def search_people():


window.mainloop()