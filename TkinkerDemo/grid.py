from tkinter import *

root = Tk()

# Label(root, text='first').pack()

Label(root, text='frist').grid(row=0)
Label(root, text='second').grid(row=1)


def getStr(event):
    print(repr(event.char))

e1 = Entry(root)
e2 = Entry(root)


def callback():
    print(e1.get())
    print(e2.get())

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
Button(root, text='OK', command=callback).grid(row=2)


root.mainloop()

