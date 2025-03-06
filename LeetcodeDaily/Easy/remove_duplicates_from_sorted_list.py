"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1 = head

        while p1 != None:
            p2 = p1
            c = 0
            while p2 != None and p2.val == p1.val:
                c += 1
                p2 = p2.next

            # duplicates present
            if c > 1:
                p1.next = p2

            p1 = p1.next

        return head
