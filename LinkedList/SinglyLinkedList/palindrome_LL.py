"""
Given a singly linked list A, determine if it's a palindrome. Return 1 or 0, denoting if it's a palindrome or not, respectively.
"""
from LinkedList.SinglyLinkedList.implement import ListNode


def palindrome_ll(A: ListNode):
    temp = A
    l = 0
    while temp != None:
        temp = temp.next
        l += 1

    if l == 1:
        return 1

    mid = l // 2 if l % 2 == 0 else (l // 2 + 1)
    head2 = A
    for i in range(mid):
        head2 = head2.next

    # reverse ll 2
    prev = None
    curr = head2
    while curr != None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    head2 = prev

    head1 = A
    while head1 != None and head2 != None:
        if head1.data != head2.data:
            return 0
        head1 = head1.next
        head2 = head2.next

    return 1
