"""
https://leetcode.com/problems/search-insert-position/
"""

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start < end:
            mid = (start + end) // 2

            if target <= nums[mid]:
                end = mid
            else:
                start = mid + 1

        if target > nums[start]:
            return start + 1
        else:
            return start
