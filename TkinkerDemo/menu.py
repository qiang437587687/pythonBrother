from tkinter import *

def callback():
    print('11235')

root = Tk()

menu = Menu(root)

root.config(menu=menu)

fileMenu = Menu(menu)
menu.add_cascade(label='File', menu=fileMenu)
fileMenu.add_command(label='New', command=callback)
fileMenu.add_command(label='New1', command=callback)
fileMenu.add_command(label='New2', command=callback)
fileMenu.add_separator()
fileMenu.add_command(label='New3', command=callback)

helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About', command=callback)

root.mainloop()