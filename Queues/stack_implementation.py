# we will the python inbuilt list as stack to implment queues


class Queue:
    def __init__(self, size):
        # we will need two stack to do queue operations
        self.st1 = list()  # push here
        self.st2 = list()  # pop from here
        self.size = size

    def enqueue(self, x) -> int:
        if (len(self.st1) + len(self.st2)) == self.size:  # queue is full
            return -1

        self.st1.append(x)

        return x

    def dequeue(self) -> int:
        if (len(self.st1) + len(self.st2)) == 0:  # queue is empty nothing to remove
            return -1

        if len(self.st2) == 0:
            # move all elemets from st1 to st2
            while len(self.st1) != 0:
                val = self.st1.pop()
                self.st2.append(val)

        # then pop
        k = self.st2.pop()

        return k

    def peek(self) -> int:  # get the element at the front of the queue
        if (len(self.st1) + len(self.st2)) == 0:
            return -1

        if len(self.st2) == 0:
            return self.st1[0]

        return self.st2[-1]


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
