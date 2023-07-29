class ListNode:
    def __init__(self, val):
        self.data = val
        self.next = None


class Stack:
    def __init__(self):
        self.cnt = 0
        self.head = None

    def push(self, x) -> None:
        nn = ListNode(x)
        if self.head == None:
            self.head = nn
        else:
            nn.next = self.head
            self.head = nn

        self.cnt += 1

    def pop(self) -> int:
        if self.head == None:
            return -1

        k = self.head.data
        self.head = self.head.next
        self.cnt -= 1
        return k

    def peek(self) -> int:
        if self.head == None:
            return -1
        return self.head.data

    def size(self) -> int:
        return self.cnt


# test case
# create stack of [1,2,3,4]
st = Stack()
st.push(1)
st.push(2)
st.push(3)
st.push(4)

assert st.peek() == 4
assert st.size() == 4

st.pop()

assert st.peek() == 3
assert st.size() == 3

st.pop()

assert st.peek() == 2
assert st.size() == 2

st.pop()

assert st.peek() == 1
assert st.size() == 1

st.pop()

assert st.peek() == -1
assert st.size() == 0
