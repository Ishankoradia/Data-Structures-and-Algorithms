class Queue:
    def __init__(self, size):
        self.front = -1  # the index where the last element was removed from
        self.back = -1  # the index where the last element was appended/pushed
        self.arr = [None] * size
        self.cnt = 0  # to track the size of the queue, how much filled it is
        self.size = size

    def enqueue(self, x) -> int:
        if self.cnt == self.size:  # queue is full
            return -1

        # we can push elements circularly
        self.back = (self.back + 1) % self.size

        self.arr[self.back] = x
        self.cnt += 1

        return x

    def dequeue(self) -> int:
        if self.cnt == 0:  # queue is empty nothing to remove
            return -1

        # if you are the end, go the first element and pop
        self.front = (self.front + 1) % self.size
        self.cnt -= 1
        return self.arr[self.front]

    def peek(self) -> int:  # get the element at the front of the queue
        if self.cnt == 0:
            return -1

        return self.arr[(self.front + 1) % self.size]


# test cases
que = Queue(5)

que.enqueue(1)
assert que.peek() == 1

que.enqueue(2)
assert que.peek() == 1

que.enqueue(3)
assert que.peek() == 1

que.enqueue(4)
assert que.peek() == 1

que.enqueue(5)
assert que.peek() == 1

# que is full
assert que.enqueue(6) == -1

# remove
que.dequeue()
assert que.peek() == 2

# que is not full
assert que.enqueue(6) == 6

# que is full
assert que.enqueue(6) == -1

# remove
que.dequeue()
assert que.peek() == 3
que.dequeue()
assert que.peek() == 4
que.dequeue()
assert que.peek() == 5
que.dequeue()
assert que.peek() == 6
que.dequeue()

# que is empty
assert que.dequeue() == -1
