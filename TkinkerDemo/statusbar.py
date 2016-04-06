from tkinter import *

root = Tk()

vars = StringVar()

# v = StringVar()
# Label(master, textvariable=v).pack()
# v.set("New Text!")

status = Label(root, textvariable=vars, borderwidth=1, relief=SUNKEN, anchor=W) # 自己的样式
vars.set('nimeia')
status.pack(side=BOTTOM, fill=X)  # 显示的样式


def callback():
    print('123456789')
    vars.set('23456743fdgsjfgdsljgs')

b = Button(root, text='button', command=callback)
b.pack()

root.mainloop()
