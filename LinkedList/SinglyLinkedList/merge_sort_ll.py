"""
Sort a linked list, A in O(n log n) time.
"""

from LinkedList.SinglyLinkedList.implement import ListNode
from LinkedList.SinglyLinkedList.middle_element_ll import middle_ele_ll
from LinkedList.SinglyLinkedList.merge_two_sorted_ll import merge_ll


def sort1(A: ListNode):
    if A is None:
        return A

    mid: ListNode = middle_ele_ll(A)

    h1 = sort1(mid.next)

    mid.next = None

    h2 = sort1(A)

    return merge_ll(h1, h2)
