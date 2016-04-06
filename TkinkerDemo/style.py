
from tkinter import *

button = Button(text='zhangxianqiang', padx=10, pady=30)  # 距离x 轴的边距
button.config(cursor='gumby')

button.config(borderwidth=20, relief=RIDGE)
button.config(bg='Green', fg='Yellow')
button.config(font=("Helvetica", 30, "bold italic"))

button.pack()
button.mainloop()






