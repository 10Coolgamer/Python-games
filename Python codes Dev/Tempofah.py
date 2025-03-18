from tkinter import *
import tkinter.font as font
root=Tk()
root.title("Celsius to Fahrenheit Converter")
root.config(background="teal")
root.geometry("700x300")
def convert():
    t=c.get()
    if(t.replace('.','',1).isdigit()):
        e.grid_forget()
        fah=(float(t)*9/5)+32
        o.config(text="Temperature in Fahrenheit:"+str(fah))
    else:
        e.grid(row=1,column=1)
d=Label(root,text="Celsius --> Fahrenheit",font=("Impact",30,"bold"),bg="teal",fg="white")
d.pack()
frame=Frame(root)
frame.pack(padx=5,pady=20)
m=Label(frame,text="Enter temperature in Celsius",font=("Impact",25),bg="teal",fg="white")
m.grid(row=0,column=0)
c=Entry(frame,font=("Impact",20))
c.grid(row=0,column=1)
e=Label(frame,text="Erorr... Enter valid input",font=("Comic Sans MS",15),bg="teal",fg="red")
o=Label(frame,font=("Comic Sans MS",15),bg="teal")
o.grid(row=2,column=0,columnspan=2,pady=10)
submit=Button(frame,text="Convert",width=30,font=("Impact",30),bg="teal",fg="white",command=convert)
submit.grid(row=3,column=0,columnspan=2,pady=10)

root.mainloop()