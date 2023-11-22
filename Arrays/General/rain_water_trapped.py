"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.

Example:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

"""


def trap(height) -> int:
    N = len(height)
    left_max = [0 for _ in range(N)]
    left_max[0] = height[0]
    for i in range(1, N):
        left_max[i] = max(left_max[i - 1], height[i])

    right_max = [0 for _ in range(N)]
    right_max[N - 1] = height[N - 1]
    for i in range(N - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], height[i])

    water_trapped = 0
    for i in range(N):
        water_trapped += min(left_max[i], right_max[i]) - height[i]

    return water_trapped
