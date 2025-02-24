"""
https://leetcode.com/problems/two-sum/description/
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # bruteforce
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if (nums[i] + nums[j]) == target:
        #             return [i, j]

        # optimized approach

        # since there is a valid answer always
        if len(nums) == 2:
            return [0, 1]

        hashmap = dict()  # store h[value] = index
        for i in range(len(nums)):
            if (target - nums[i]) in hashmap:
                return [i, hashmap[target - nums[i]]]

            hashmap[nums[i]] = i
