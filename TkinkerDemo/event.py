from tkinter import *
import tkinter.messagebox

root = Tk()

# def button1Click():
#     print('zhang')
#
# button = Button(text='hello', command=button1Click) # 简单事件回调  方法1
# button.pack()
# root.mainloop()


def callback(event):
    frame.focus_set()
    print('click at : ', event.x, event.y)


def key(event):
    print('pressed', repr(event.char))  # 得到 键盘输入的 内容.  方法2


def closewindow():
    if tkinter.messagebox.askokcancel('请认真选择', '你傻吗?'):
        root.destroy()


frame = Frame(root, width=100, height=100)  # 事件绑定.
frame.bind('<Button-1>', callback)
frame.bind('<Key>', key)
frame.pack()


root.protocol('WM_DELETE_WINDOW', closewindow)

root.mainloop()

