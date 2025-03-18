from tkinter import *

root = Tk()

root.geometry("500x500")
root.title("Things")
root.config(background="black")

blc=Button(root,text="Click Me...",bd='6',background="teal",command=root.destroy)
blc.pack(side='top')
blc=Button(root,text="Please click Me...",bd='7',background="orange",command=root.destroy)
blc.pack(side='bottom')
blc=Button(root,text="Please x 10 click Me...",bd='8',background="blue",command=root.destroy)
blc.pack(side='right')
blc=Button(root,text="Please don't click Me...",bd='9',background="green",command=root.destroy)
blc.pack(side='left')
root.mainloop()

