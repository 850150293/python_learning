import tkinter as tk

window = tk.Tk()
window.geometry('200x200')

tk.Label(window,text='my frame',width=20).pack()

fm = tk.Frame(window)
fm.pack()

fm_l = tk.Frame(fm)
fm_r = tk.Frame(fm)

fm_l.pack(side='left')
fm_r.pack(side='right')

tk.Label(fm,text='main frame').pack()
tk.Label(fm_l,text='left').pack()
tk.Label(fm_r,text='right').pack()

window.mainloop()
