from tkinter import *
from tkinter.ttk import *

root = Tk()

progress=Progressbar(root,orient=HORIZONTAL,length=100,mode='determinate')

def bar():
    import time
    progress['value']=20
    root.update_idletasks()
    time.sleep(1)
    
    progress['value']=40
    root.update_idletasks()
    time.sleep(1)
    
    progress['value']=50
    root.update_idletasks()
    time.sleep(1)
    
    progress['value']=60
    root.update_idletasks()
    time.sleep(1)
    
    progress['value']=80
    root.update_idletasks()
    time.sleep(1)
    
    progress['value']=100 
      
progress.pack(pady=10)

Button(root,text='Begin',command=bar).pack(pady=10)


mainloop()