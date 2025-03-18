from tkinter import *

root = Tk()
root.title("My Favorite games")

listbox=Listbox(root,height=10,width=15,bg='gray',activestyle='dotbox',font='Impact',fg='orange')
root.geometry("300x250")

label=Label(root, text='Favorite Games')

listbox.insert(1, "Gensin Impact")
listbox.insert(2, "Minecraft")
listbox.insert(3, "Roblox")
listbox.insert(4, "Brawl Stars")
listbox.insert(5, "Luis adventures")

label.pack()
listbox.pack()

root.mainloop()