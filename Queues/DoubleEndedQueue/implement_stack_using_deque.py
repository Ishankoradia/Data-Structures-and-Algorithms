from collections import deque


class Stack:
    def __init__(self):
        self.deq = deque()

    def push(self, val):
        self.deq.append(val)

    def peek(self):
        if len(self.deq) == 0:
            return -1

        return self.deq[-1]

    def pop(self):
        if len(self.deq) == 0:
            return -1

        return self.deq.pop()
