#Import module
from tkinter import*
from tkinter.ttk import *
#Import strf function revive sistum time
from time import strftime
#Root window
clock=Tk()
clock.title("Clock")
#Display time
def time():
    string=strftime('%H:%M:%S:%p')
    display.config(text=string)
    display.after(1000,time)
#creating and styling 
display=Label(clock,font=("Impact",200,"bold"),background="orange",foreground="blue")
#Placing clock in middle
display.pack(anchor="center")
#calling function
time()
#running the code
clock.mainloop()