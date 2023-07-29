# A double ended queue has the feature of adding and removing elements from either end

from collections import deque


deq = deque()

# insert on the right
deq.append(1)  # [1]
assert deq[0] == 1
assert deq[-1] == 1


# insert on the left
deq.appendleft(2)  # [2,1]
assert deq[0] == 2
assert deq[-1] == 1

assert len(deq) == 2

# pop from right
deq.pop()  # [2]
assert deq[0] == 2
assert deq[-1] == 2

# insert on the left
deq.appendleft(1)  # [1,2]
assert deq[0] == 1
assert deq[-1] == 2

# pop from left
assert deq[0] == 2
assert deq[-1] == 2

# pop from left
deq.popleft()
assert len(deq) == 0
