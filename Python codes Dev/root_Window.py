from tkinter import *
root=Tk()
root.title("Yellow window")
root.resizable(False,False)
root.config(bg="Yellow")
a=Label(root,text="Yellow root window",bg="yellow",fg="Black",font=("Pixel",30))
a.grid(row=0,column=0)
b=Label(root,text="Is 1 an even or odd number",bg="yellow",fg="Black",font=("Pixel",12))
b.grid(row=1,column=0)
def no():
    f=Label(root,text="You got it correct!", bg="yellow",font=("Pixel",12))
    f.grid(row=3,column=0)
def ne():
    g=Label(root,text="You got it incorrect.", bg="yellow",font=("Pixel",12))
    g.grid(row=3,column=0)
c=Button(root,text="Even",bg="yellow",fg="Black",font=("Pixel",12), command=ne)
c.grid(row=2,column=0)
d=Button(root,text="Odd",bg="yellow",fg="Black",font=("Pixel",12),command=no)
d.grid(row=2,column=1)
root.mainloop()

