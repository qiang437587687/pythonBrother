
from tkinter import *

class App:
    def __init__(self, master):

        frame = Frame(master)

        frame.pack()

        self.button = Button(frame, text='局长继续吹', fg='red', command=frame.quit)

        self.button.pack()

        self.hiButton = Button(frame, text='吹吹吹吹', command=self.say_hi)

        self.hiButton.pack()

    def say_hi(self):

        print('局长 hihihihi')



root = Tk()
app = App(root)
root.mainloop()
# root.destory()

