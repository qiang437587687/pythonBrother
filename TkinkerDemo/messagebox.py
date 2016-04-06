from tkinter import *
import tkinter.messagebox


root = Tk()

def callback():
    print('click')
    if tkinter.messagebox.askyesno('zhangxianqiang', 'hi zhang'):  # show~~~  ask~~~
        print('yes')
    else:
        print('no')

button = Button(root, text='Button1', command=callback)
button.pack()
root.mainloop()

