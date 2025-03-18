# Import modules
from tkinter import *
import time
from tkinter import messagebox
# Root window
root=Tk()
root.geometry("600x250")
root.resizable(False,False)
root.config(background="Orange")
root.title("Timer")
hour=StringVar()
minute=StringVar()
second= StringVar()
#Configure
a=Label(root,text="Welcome to the timer app",bg="orange",fg="blue",font=("Impact",30,"bold"))
a.place(x=0,y=0)
b=Label(root,text="Enter a  time limit and set the timer by pressing the button. It will notify you when the timer is up",fg="blue",bg="orange",font=("Impact",10,"normal"))
b.place(x=0,y=50)
#set the default value to 0
hour.set("00")
minute.set("00")
second.set("00")
#Timer entrys
hourEntry=Entry(root,width=3,font=("Impact",18,"normal"),textvariable=hour)
hourEntry.place(x=0,y=100)
minuteEntry=Entry(root,width=3,font=("Impact",18,"normal"),textvariable=minute)
minuteEntry.place(x=50,y=100)
secondEntry=Entry(root,width=3,font=("Impact",18,"normal"),textvariable=second)
secondEntry.place(x=100,y=100)
#Code that makes the thing work
def submit1():
    try:
        #Info given by user is stored in temp
        temp=int(hour.get())*3600+int(minute.get())*60+int(second.get())
    except:
        print("Not Valid")
    while temp > -1:
        #divmod gives 2 valued the quoshent and the remainder.
        mins,sec=divmod(temp,60)
        hours=00
        if mins>60:
            hours,mins=divmod(mins,60)
            #using format metod to store up till 2 desimal places
        hour.set('{00:2d}'.format(hours))
        minute.set("{00:2d}".format(mins))
        second.set("{00:2d}".format(sec))
        #Updating the root window
        root.update()
        time.sleep(1)
        if (temp==0):
            messagebox.showinfo("Timer Countdown","Time's up")
        temp=temp-1 
#Button to start
btn=Button(root,text='Set Time Countdown',bd="5",command=submit1)
btn.place(x=0,y=150)
#To run the code
root.mainloop()