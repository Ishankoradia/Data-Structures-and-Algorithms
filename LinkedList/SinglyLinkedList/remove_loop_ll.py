"""
You are given a linked list that contains a loop.
You need to find the node, which creates a loop and break it by making the node point to NULL.

"""


def solve(A):
    fast = A
    slow = A

    if fast.next == None:
        return A

    fast = fast.next.next
    slow = slow.next

    while fast != slow or fast != None:
        fast = fast.next.next
        slow = slow.next

    slow = A

    while slow.next != fast.next:
        slow = slow.next
        fast = fast.next

    fast.next = None

    return A
