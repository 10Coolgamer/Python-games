from tkinter import *
from tkinter import ttk
root=Tk()
root.title("Weight Converter")
root.resizable(False,False)
entry=Entry(root)
entry.grid(row=1,column=0,padx=10,pady=10)
root.config(background="orange")
def convert():
    try:
        weight=float(entry.get())
        from_unit=from_combo.get()
        to_unit=to_combo.get()
        convershion_factors={
            "Pounds":0.453592,
            "Kilograms":1.0,
            "Ounces":0.0283495,
            "Grams":0.001
        }
        weight_in_kg=weight*convershion_factors[from_unit]
        converted_weight=weight_in_kg/convershion_factors[to_unit]
        result_label.config(text=f"converted:{converted_weight:4f}{to_unit}")
    except ValueError:
        result_label.config(text="Invalid input")
lable=Label(root,text="Weight Converter",font=("Impact",30,"normal"),bg="orange")
lable.grid(row=0,column=0,columnspan=4,pady=10)
units=['Pounds',"Kilograms",'Ounces','Grams']
from_combo=ttk.Combobox(root,values=units,state="readonly")
from_combo.grid(row=1,column=1,padx=10)
from_combo.set('Pounds')
to_combo=ttk.Combobox(root,values=units,state="readonly")
to_combo.grid(row=1,column=3,padx=10)
to_combo.set('Kilograms')
convert_button=Button(root,text="Convert",command=convert)
convert_button.grid(row=1,column=2,padx=10)
result_label=Label(root,text="")
result_label.grid(row=2,column=0,columnspan=4,pady=10)
root.mainloop()