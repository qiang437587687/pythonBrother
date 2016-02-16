#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# print("tkinter GUI 编程")

from tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.creatWidgets()

    def creatWidgets(self):
        self.helloLabel = Label(self, text='和尚傻')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='是的', command=self.quit)
        self.quitButton.pack()


app = Application()
# 设置窗口标题:
app.master.title('问一个问题')
# 主消息循环:
app.mainloop()



