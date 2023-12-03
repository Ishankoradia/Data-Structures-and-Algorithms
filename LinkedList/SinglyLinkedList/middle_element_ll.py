"""
Given a linked list of integers, find and return the middle element of the linked list.

NOTE: If there are N nodes in the linked list and N is even then return the (N/2 + 1)th element.
"""


def solve(A):
    fast = A
    slow = A

    while fast != None and fast.next != None:
        fast = fast.next.next
        slow = slow.next

    return slow.val
