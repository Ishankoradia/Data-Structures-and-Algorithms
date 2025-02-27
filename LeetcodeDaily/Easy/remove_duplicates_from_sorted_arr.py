"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # not memory optimized
        # s1 = set()
        # unique = list()

        # for i in range(len(nums)):
        #     if nums[i] not in s1:
        #         unique.append(nums[i])
        #     s1.add(nums[i])

        # for i in range(len(unique)):
        #     nums[i] = unique[i]

        # return len(unique)

        # two pointer approach
        curr = 0
        k = 0
        while curr < len(nums):
            unique_ele = nums[curr]
            while curr < len(nums) and nums[curr] == unique_ele:
                curr += 1

            nums[k] = unique_ele
            k += 1

        return k
