from tkinter import *
import calendar
def showcal():
    root=Tk()
    root.config(background="#ff4200")
    root.title("CALENDER")
    root.geometry("550x600")
    fetch_year=int(year_field.get())
    cal_content= calendar.calendar(fetch_year)
    cal_year=Label(root, text=cal_content, font="Consolas 10 bold")
    cal_year.grid(row=5, column=1, padx=20, pady=20)
    root.mainloop
if   __name__ == "__main__":
    root=Tk()
    root.config(background="Blue")
    root.title("CALENDER")
    root.geometry("250x140")
    cal=Label(root, text="Calender",bg="green",font=("BLOKK",28,"bold"), anchor="center", justify="center")
    year=Label(root,text="ENTER YEAR", bg="Red")
    year_field=Entry(root)
    show=Button(root,text="Show Calender", fg="yellow",bg="Purple",command=showcal)
    Exit=Button(root,text="Exit",fg="white",bg="Orange",command=exit)
    cal.pack()
    year.pack()
    year_field.pack()
    show.pack()
    Exit.pack()
    root.mainloop()
