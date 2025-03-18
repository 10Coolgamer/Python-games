from tkinter import *
root=Tk()
root.resizable(False,False)
root.geometry("600x650")
root.config(bg="Light green")
root.title("Pocket Money Saver")
h=0
i=0
j=0
k=100
def Food_money():
    global h, k
    h=h+20
    k=k-20
    f.config(text="$"+str(k))
    g.config(text="Amount for food=$"+str(h))
def Cloths_money():
    global i, k
    i=i+15
    k=k-15
    f.config(text="$"+str(k))
    l.config(text="Amount for Cloths=$"+str(i))
def Toys_money():
    global j, k
    j=j+7
    k=k-7
    f.config(text="$"+str(k))
    m.config(text="Amount for Toys=$"+str(j))
def restart():
    global h,i,j,k
    h=0
    i=0
    j=0
    k=k+100
    f.config(text="$"+str(k))
    m.config(text="Amount for Toys=$"+str(j))
    l.config(text="Amount for Cloths=$"+str(i))
    g.config(text="Amount for food=$"+str(h))
    root.update()
a=Label(root,text="Pocket Money Manager",bg="Light green",fg="Dark green",font=("Impact",30))
a.place(x=0,y=100)
b=Button(root,text="Food",bg="light green",fg="Dark green",font=("Impact",12),command=Food_money)
b.place(x=20,y=200)
c=Button(root,text="Cloths",bg="light green",fg="Dark green",font=("Impact",12),command=Cloths_money)
c.place(x=70,y=200)
d=Button(root,text="Toys",bg="light green",fg="Dark green",font=("Impact",12),command=Toys_money)
d.place(x=133,y=200)
e=Button(root,text="Start for next month",bg="Light green",fg="Dark green",font=("Impact",20),command=restart)
e.place(x=20,y=300)
f=Label(root,text="$"+str(k),bg="light green",fg="Dark green",font=("Impact",17))
f.place(x=20,y=250)
g=Label(root,text="Amount for food=$"+str(h),bg="Light green",fg="Dark green",font=("Impact",12))
g.place(x=20,y=400)
l=Label(root,text="Amount for cloths=$"+str(i),bg="Light green",fg="Dark green",font=("Impact",12))
l.place(x=20,y=430)
m=Label(root,text="Amount for Toys=$"+str(j),bg="Light green",fg="Dark green",font=("Impact",12))
m.place(x=20,y=460)
root.mainloop()