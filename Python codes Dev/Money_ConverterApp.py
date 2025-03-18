from tkinter import *
from tkinter import ttk
root=Tk()
root.title("Money converter")
root.config(background="orange")
root.resizable(False,False)
def convert():
    try:
        money=float(c.get())
        from_unit=from_combo.get()
        to_unit=to_combo.get()
        convershion={
            "Rupee":0.012,
            "Dollars":1,
            "Euro":0.97,
            "Pound":0.82
        }
        money_in_dollar=money*convershion[from_unit]
        conveted=money_in_dollar/convershion[to_unit]
        e.config(text=f"conveted:{conveted:4f}{to_unit}")
    except ValueError:
        e.config(text="Invalid input")  
a=Label(root,text="Money converter",font=("Impact",30,"normal"),fg="gray")
a.grid(row=0,column=1,padx=10)
units=["Rupee","Dollars","Euro","Pound"]
from_combo=ttk.Combobox(root,values=units,state="readonly")
from_combo.grid(row=1,column=1)
from_combo.set('Pound')
to_combo=ttk.Combobox(root,values=units,state="readonly")
to_combo.grid(row=1,column=3)
to_combo.set("Dollars")
c=Entry(root)
c.grid(row=1,column=0,pady=2)
b=Label(root,text="to",font=("Impact",12,"normal"))
b.grid(row=1,column=2,padx=10)
d=Button(root,text="Submit",font=("Impact",12,"normal"),fg="gray",command=convert)
d.grid(row=2,column=1)
e=Label(root,font=("Impact",12,"normal"),fg="gray")
e.grid(row=3,column=3)
root.mainloop()