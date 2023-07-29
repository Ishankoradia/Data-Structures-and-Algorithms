class ListNode:
    def __init__(self, val):
        self.data = val
        self.next = None


class Queue:
    def __init__(self, size):
        # two dummy nodes for tail and head to start with
        self.head = None
        self.tail = None
        self.cnt = 0  # to track the size of the queue, how much filled it is
        self.size = size

    def enqueue(self, x) -> int:
        if self.cnt == self.size:  # queue is full
            return -1

        nn = ListNode(x)
        if self.head is None:
            self.head = nn
            self.tail = nn
        else:
            self.tail.next = nn
            self.tail = nn
        self.cnt += 1
        return nn.data

    def dequeue(self) -> int:
        if self.cnt == 0:  # queue is empty nothing to remove
            return -1

        k = self.head.data
        self.head = self.head.next
        self.cnt -= 1
        return k

    def peek(self) -> int:  # get the element at the front of the queue
        if self.cnt == 0:
            return -1

        return self.head.data


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
