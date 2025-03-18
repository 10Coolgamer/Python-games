from tkinter import*
root=Tk()
root.geometry("600x550")
root.config(bg="light blue")
root.resizable(False,False)
root.title=("Vacation savings")
food=0
hotel=0
parks=0
shopping=0
total=1000
def Food():
    global food,total
    food=food+60
    total=total-60
    f.config(text="$"+str(total))
    g.config(text="Amount for food=$"+str(food))
    if total<=0:
        root.config(bg="Red")
    elif total>0:
        root.config(bg="light blue")
def Hotel():
    global hotel,total
    hotel=hotel+100
    total=total-100
    f.config(text="$"+str(total))
    l.config(text="Amount for hotels=$"+str(hotel))
    if total<=0:
        root.config(bg="Red")
    elif total>0:
        root.config(bg="light blue")
def park():
    global parks,total
    parks=parks+350
    total=total-350
    f.config(text="$"+str(total))
    m.config(text="Amount for parks=$"+str(parks))
    if total<=0:
        root.config(bg="Red")
    elif total>0:
        root.config(bg="light blue")
def shoping():
    global shopping,total
    shopping=shopping+40
    total=total-40
    f.config(text="$"+str(total))
    y.config(text="Amount for shopping=$"+str(shopping))
    if total<=0:
        root.config(bg="Red")
    elif total>0:
        root.config(bg="light blue")
def restart():
    global food,hotel,parks,shopping,total
    food=0
    hotel=0
    parks=0
    shopping=0
    total=total+1000
    f.config(text="$"+str(total))
    m.config(text="Amount for hotels=$"+str(hotel))
    l.config(text="Amount for parks=$"+str(parks))
    g.config(text="Amount for food=$"+str(food))
    y.config(text="Amount for shopping=$"+str(shopping))
    if total<=0:
        root.config(bg="Red")
    elif total>0:
        root.config(bg="light blue")
a=Label(root,text="Vacation money manager",bg="light blue",fg="Dark blue",font=("Impact",30))
a.place(x=0,y=100)
b=Button(root,text="Food",bg="light blue",fg="Dark blue",font=("Impact",12),command=Food)
b.place(x=20,y=200)
c=Button(root,text="Hotel",bg="light blue",fg="Dark blue",font=("Impact",12),command=Hotel)
c.place(x=70,y=200)
d=Button(root,text="Parks",bg="light blue",fg="Dark blue",font=("Impact",12),command=park)
d.place(x=133,y=200)
q=Button(root,text="Shopping",bg="light blue",fg="Dark blue",font=("Impact",12),command=shoping)
q.place(x=190,y=200)
e=Button(root,text="Start for next vacation",bg="Light blue",fg="Dark blue",font=("Impact",20),command=restart)
e.place(x=20,y=300)
f=Label(root,text="$"+str(total),bg="light blue",fg="Dark blue",font=("Impact",17))
f.place(x=20,y=250)
g=Label(root,text="Amount for food=$"+str(food),bg="Light blue",fg="Dark blue",font=("Impact",12))
g.place(x=20,y=400)
l=Label(root,text="Amount for hotels=$"+str(hotel),bg="Light blue",fg="Dark blue",font=("Impact",12))
l.place(x=20,y=430)
m=Label(root,text="Amount for parks=$"+str(parks),bg="Light blue",fg="Dark blue",font=("Impact",12))
m.place(x=20,y=460)
y=Label(root,text="Amount for shopping=$"+str(shopping),bg="Light blue",fg="Dark blue",font=("Impact",12))
y.place(x=20,y=490)
root.mainloop()