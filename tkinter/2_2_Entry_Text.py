import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('300x200')

e = tk.Entry(window,show='*')
e.pack()


def insert_point():
    var = e.get();
    t.insert('insert',var)

def insert_end():
    var = e.get()
    #t.insert('end',var)
    t.insert(1.2,var)
b1 = tk.Button(window,text='insert point',height=1,width=15,command=insert_point)
b1.pack()

b2 = tk.Button(window,text='insert end',height=1,width=10,command=insert_end)
b2.pack()

t = tk.Text(window,height=1)
t.pack()

window.mainloop()
