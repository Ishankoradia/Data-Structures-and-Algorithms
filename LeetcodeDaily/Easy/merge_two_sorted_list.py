"""
https://leetcode.com/problems/merge-two-sorted-lists/description/
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        p1 = list1
        p2 = list2
        p3 = ListNode()

        curr = p3
        while p1 != None and p2 != None:
            if p1.val < p2.val:
                curr.next = p1
                p1 = p1.next
            else:
                curr.next = p2
                p2 = p2.next

            curr = curr.next

        if p1 != None:
            curr.next = p1

        if p2 != None:
            curr.next = p2

        return p3.next
