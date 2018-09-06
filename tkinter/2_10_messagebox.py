import tkinter as tk
import tkinter.messagebox

window = tk.Tk()
window.geometry('200x200')

def print_message():
    tk.messagebox.showinfo(title='hi',message='hello world')
    #tk.messagebox.showwarning(title='hi',message='hello world')
    #tk.messagebox.showerror(title='hi',message='hello world')
    #print(tk.messagebox.askquestion(title='hi',message='hello world'))
    #print(tk.messagebox.askyesno(title='hi',message='hello world'))
    ##print(tk.messagebox.asktrycancel(title='hi',message='hello world'))
    #print(tk.messagebox.askokcancel(title='hi',message='hello world'))
    #print(tk.messagebox.askyesnocancel(title='hi',message='hello world'))


b1 = tk.Button(window,text='show message',command = print_message)
b1.pack()



window.mainloop()
