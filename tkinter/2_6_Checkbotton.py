import tkinter as tk

window = tk.Tk()
window.title('title')
window.geometry('200x200')

l = tk.Label(window,width=10,text='empty',bg='yellow')
l.pack()

var1 = tk.IntVar()
var2 = tk.IntVar()

def print_selection():
    if((var1.get()==1)&(var2.get()==0)):
        l.config(text='python')
    elif((var1.get()==0)&(var2.get()==1)):
        l.config(text='c++')
    elif((var1.get()==0)&(var2.get()==0)):
        l.config(text='neither')
    else:
        l.config(text='both')
c1 = tk.Checkbutton(window,text='python',variable=var1,onvalue=1,offvalue=0,command = print_selection)
c1.pack()

c2 = tk.Checkbutton(window,text='c++',variable=var2,onvalue=1,offvalue=0,command = print_selection)
c2.pack()

window.mainloop()
