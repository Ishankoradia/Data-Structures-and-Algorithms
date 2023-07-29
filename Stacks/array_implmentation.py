# using the in built list/array in python
# you can also just use the following functions of the list inteasd of implementing the stack
# list().append(x)
# list().pop()
# list()[-1]


class Stack:
    def __init__(self):
        self.arr = list()

    def push(self, val):
        self.arr.append(val)

    def peek(self):
        if len(self.arr) == 0:
            return -1

        return self.arr[-1]

    def pop(self):
        if len(self.arr) == 0:
            return -1

        k = self.arr[-1]
        self.arr.pop()
        return k
