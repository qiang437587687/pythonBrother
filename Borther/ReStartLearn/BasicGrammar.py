


print('重新学习一下基础语法')

for i in range(0, 100):
    print('item %d' % i)

print('')


# 实现一个栈

class Stack():
    def __init__(self, size):
        self.stack = []
        self.size = size
        self.top = -1

    def Full(self):
        if self.top==self.size:

            return True
        else:
            return False


    def Push(self, content):
        if self.Full():
            print('stack is full!')
        else:
            self.stack.append(content)
            self.top = self.top + 1

    def Empty(self):
        if self.top == -1:
            print("stack is empty!")
            return True
        else:
            print('stack Not empty')
            return False

    def Out(self):
        if self.Empty():
            print('empty')
            return None
        else:
            self.top = self.top - 1
            return self.stack[self.top]


q = Stack(3)
q.Empty()

q.Push('hello')
q.Empty()

print(q.Out())