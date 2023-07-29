from queue import Queue


# test cases
que = Queue(maxsize=5)

que.put(1)
assert que.queue[0] == 1

que.put(2)
assert que.queue[0] == 1

que.put(3)
assert que.queue[0] == 1

que.put(4)
assert que.queue[0] == 1

print("size: ", que.qsize())

que.put(5)
assert que.queue[0] == 1

# que is full
assert que.full()

# remove
assert que.get() == 1
assert que.queue[0] == 2

# que is not full
que.put(6)

# que is full
assert que.full()

# remove
que.get()
assert que.queue[0] == 3
que.get()
assert que.queue[0] == 4
que.get()
assert que.queue[0] == 5
que.get()
assert que.queue[0] == 6
que.get()

# que is empty
assert que.empty()
