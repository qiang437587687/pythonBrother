# __author__ = 'Zhang'

from tkinter import *

root = Tk()

label = Label(root, text='局长别吹牛逼')

# label.config()


label.config(cursor='gumby')
label.config(width=30, height=5, fg='orange', bg='dark green')
label.config(font=('times', '28', 'bold'))


label.pack()  # 呈现出来
root.mainloop()  # 死循环 一直显示.
