"""
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.
"""


def firstMissingPositive(nums) -> int:
    N = len(nums)
    for i in range(N):
        j = i
        while nums[i] > 0 and nums[i] <= N and nums[i] != nums[nums[i] - 1]:
            # swap A[j] with A[A[j]-1]
            temp = nums[i]
            nums[i] = nums[temp - 1]
            nums[temp - 1] = temp

    for i in range(N):
        if nums[i] != i + 1:
            return i + 1

    return N + 1
