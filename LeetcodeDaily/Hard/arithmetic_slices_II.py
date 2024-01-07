"""
Given an integer array nums, return the number of all the arithmetic subsequences of nums.

A sequence of numbers is called arithmetic if it consists of at least three elements ,
and if the difference between any two consecutive elements is the same.

For example, [1, 3, 5, 7, 9], [7, 7, 7, 7], and [3, -1, -5, -9] are arithmetic sequences.
For example, [1, 1, 2, 5, 7] is not an arithmetic sequence.
A subsequence of an array is a sequence that can be formed by 
removing some elements (possibly none) of the array.

For example, [2,5,10] is a subsequence of [1,2,1,2,4,1,5,10].
The test cases are generated so that the answer fits in 32-bit integer.

EXAMPLE:
    Input: nums = [2,4,6,8,10]
    Output: 7
    Explanation: All arithmetic subsequence slices are:
    [2,4,6]
    [4,6,8]
    [6,8,10]
    [2,4,6,8]
    [4,6,8,10]
    [2,4,6,8,10]
    [2,6,10]


"""
import time


def numberOfArithmeticSlices(nums: list) -> int:
    # brute force; TC: O(2^n) SC: O(n)
    N = len(nums)

    def cntAP(j, diff, nums=nums):
        if j == len(nums):
            return 0

        cnt = 0
        for k in range(j + 1, N):
            if (nums[k] - nums[j]) == diff:
                cnt += 1 + cntAP(k, diff)

        return cnt

    cnt = 0
    for i in range(N):
        for j in range(i + 1, N):
            cnt += cntAP(j, nums[j] - nums[i])

    return cnt


def numberOfArithmeticSlices_v1(nums: list) -> int:
    # optimized force; TC: O(n^2) SC: O(n^2)
    N = len(nums)
    global dp
    dp = [dict() for i in range(N)]
    global ans
    ans = 0
    # dp[i][diff] will give me the number of weak (basically also of length 2)
    # arithmetic subsequences ending at index i with differnce diff

    def cntAP(j, nums=nums):
        global dp
        global ans

        if j == 0:
            return 0

        if j == len(nums):
            return 0

        for i in range(0, j):
            curr_diff = nums[j] - nums[i]
            if curr_diff in dp[i]:  # we can extend subsequence ending at i with diff d
                dp[j][curr_diff] = dp[j].get(curr_diff, 0) + dp[i][curr_diff]
                ans = ans + dp[i][curr_diff]

            # add weak subsequence
            dp[j][curr_diff] = dp[j].get(curr_diff, 0) + 1

    for i in range(N):
        cntAP(i, nums=nums)

    return ans


assert numberOfArithmeticSlices([1, 1, 2, 3, 4, 5]) == 11
assert numberOfArithmeticSlices_v1([1, 1, 2, 3, 4, 5]) == 11

assert numberOfArithmeticSlices([2, 4, 6, 8, 10]) == 7
assert numberOfArithmeticSlices_v1([2, 4, 6, 8, 10]) == 7

start1 = time.time()
assert (
    numberOfArithmeticSlices(
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    )
    == 4194050
)
end1 = time.time()
start2 = time.time()
assert (
    numberOfArithmeticSlices_v1(
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    )
    == 4194050
)
end2 = time.time()


# check time of brute vs optimized approach
print("Brute force : ", end1 - start1)
print("Optimized approach : ", end2 - start2)
