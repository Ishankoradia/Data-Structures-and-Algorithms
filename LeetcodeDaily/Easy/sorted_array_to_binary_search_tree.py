"""
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
"""

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def arrayToBST(self, nums, start, end):
        if start > end:
            return None
        mid = (start + end) // 2

        root = TreeNode(val=nums[mid])
        root.left = self.arrayToBST(nums, start, mid - 1)
        root.right = self.arrayToBST(nums, mid + 1, end)

        return root

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.arrayToBST(nums, 0, len(nums) - 1)
