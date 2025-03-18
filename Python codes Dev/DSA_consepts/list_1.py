# Import module and root window
from tkinter import *
root=Tk()
root.geometry("300x400")
root.title("Basic Calculator")
#Settin an entry box
entry=Entry(root,width=16,font=("Pixel",12,"normal"),bd=5,relief="ridge",justify='right')
entry.grid(row=0,column=0,columnspan=4,padx=10,pady=10)
#Making functions
def click(value):
    entry.insert(END,value)
def clear():
    entry.delete(0,END)
def calculate():
    try:
        r=eval(entry.get())
        entry.delete(0,END)
        entry.insert(END,r)
    except Exception:
        entry.delete(0,END)
        entry.insert(END,"Error")
    #The list
buttons=[
    ('7','8','9','/'),
    ('4','5','6','*'),
    ('1','2','3','-'),
    ('0','C','=','+')
]
#Button creation
for r,row in enumerate(buttons):
    for c, char in enumerate(row):
        if char == 'C':
            btn=Button(root,text=char,width=5,height=2,font=("Pixel",14),command=clear,bg="black",fg="white")
        elif char == "=":
            btn=Button(root,text=char,width=5,height=2,font=("Pixel",14),command=calculate,bg="black",fg="white")
        else:
            btn=Button(root,text=char,width=5,height=2,font=("Pixel",14),command=lambda ch=char: click(ch))
        btn.grid(row=r+1,column=c,padx=5,pady=5)       
    
root.mainloop()