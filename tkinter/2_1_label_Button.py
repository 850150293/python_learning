import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('300x100')

var = tk.StringVar()

#l = tk.Label(window,text='OMG!this is TK!',bg='yellow',font=('Arial',12),width=15,height=2)
l = tk.Label(window,textvariable=var,bg='yellow',font=('Arial',12),width=15,height=2)
l.pack()


on_hit = False
def hit_me():
    global on_hit
    if on_hit==False:
        on_hit = True
        var.set('hit_me')
    else:
        var.set('')
        on_hit = False

b = tk.Button(window,text='hit me',width=15,height=1,command=hit_me)
b.pack()

window.mainloop()
