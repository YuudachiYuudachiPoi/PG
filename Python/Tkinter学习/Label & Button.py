import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x100')

l = tk.Label(window,
    text='OMG! this is TK!',
    bg='white',
    font=('Arial',12),
    width=15,height=2
    )






l.pack()
window.mainloop()