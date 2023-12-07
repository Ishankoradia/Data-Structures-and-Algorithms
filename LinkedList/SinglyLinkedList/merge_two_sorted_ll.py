"""
Merge two sorted linked lists, A and B, and return it as a new list.

The new list should be made by splicing together the nodes of the first two lists and should also be sorted.
"""
from LinkedList.SinglyLinkedList.implement import ListNode


def merge(A: ListNode, B: ListNode):
    if A == None:
        return B

    if B == None:
        return A

    head = A
    if A.data <= B.data:
        A = A.next
    else:
        head = B
        B = B.next

    temp = head

    while A != None and B != None:
        if A.data <= B.data:
            temp.next = A
            A = A.next
        else:
            temp.next = B
            B = B.next

        temp = temp.next

    if A != None:
        temp.next = A

    if B != None:
        temp.next = B

    return head
