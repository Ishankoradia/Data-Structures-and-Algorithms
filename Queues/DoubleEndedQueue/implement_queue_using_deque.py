from collections import deque


class Queue:
    def __init__(self, size):
        self.deq = deque(maxlen=size)
        self.size = size

    def enqueue(self, x) -> int:
        if len(self.deq) == self.size:  # queue is full
            return -1

        self.deq.append(x)

        return self.deq[-1]

    def dequeue(self) -> int:
        if len(self.deq) == 0:  # queue is empty nothing to remove
            return -1

        return self.deq.popleft()

    def peek(self) -> int:  # get the element at the front of the queue
        if len(self.deq) == 0:
            return -1

        return self.deq[0]


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
