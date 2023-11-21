"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.
"""


# Approach : Kadane's Algorithm
def maxSubArray(self, nums) -> int:
    max_subarray = float("-inf")
    current_subarray = 0
    for i in range(len(nums)):
        current_subarray += nums[i]

        max_subarray = max(current_subarray, max_subarray)

        if current_subarray < 0:
            current_subarray = 0

    return max_subarray
