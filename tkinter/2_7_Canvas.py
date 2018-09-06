import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('500x500')

cv = tk.Canvas(window,bg='blue',height=400,width=400)


image_file = tk.PhotoImage(file='ins.gif')
image = cv.create_image(10,10,anchor='nw',image=image_file)

x0,y0,x1,y1 = 50,50,80,80
line = cv.create_line(x0,y0,x1,y1)

oval = cv.create_oval(x0,y0,x1,y1,fill='red')
arc = cv.create_arc(x0+30,y0+30,x1+30,y1+30,start=0,extent=90)
rect = cv.create_rectangle(100,30,100+20,30+20)

cv.pack()

def moveit():
    cv.move(rect,0,2)

b1 = tk.Button(window,text='move',width=5,command=moveit)
b1.pack()

window.mainloop()
