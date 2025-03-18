from tkinter import *

root=Tk()
root.geometry("300x150")

w=Label(root,text='Chocos and IceCreams', font="50")
w.pack()

frame=Frame(root)
frame.pack()

bottomframe=Frame(root)
bottomframe.pack(side=LEFT)

b1_button= Button(frame,text="Choco",fg="red",bg="beige")
b1_button.pack(side=LEFT)

b2_button= Button(frame,text="caramel",fg="brown",bg="beige")
b2_button.pack(side=LEFT)

b3_button=Button(frame,text="Dark Choco",fg="teal",bg="beige")
b3_button.pack(side=LEFT)

b4_button=Button(bottomframe,text="Watermelon",fg="lightBlue",bg="green")
b4_button.pack(side=BOTTOM)

b5_button=Button(bottomframe,text="strawberry",fg="gray",bg="yellow")
b5_button.pack(side=BOTTOM)

b6_button=Button(bottomframe,text="Orange",fg="cyan",bg="orange")
b6_button.pack(side=BOTTOM)

root.mainloop()