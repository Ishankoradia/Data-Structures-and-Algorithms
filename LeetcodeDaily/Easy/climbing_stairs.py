"""
https://leetcode.com/problems/climbing-stairs/description/
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        # recursion
        # if n <= 0:
        #     return 0
        # elif n == 1:
        #     return 1
        # elif n == 2:
        #     return 2
        # else:
        #     return self.climbStairs(n-2) + self.climbStairs(n-1)

        # dynamic programming
        n_1 = 2  # n = 2
        n_2 = 1  # n = 1
        if n == 0:
            return 0
        if n == 1:
            return n_2
        if n == 2:
            return n_1
        for i in range(3, n + 1):
            curr = n_1 + n_2
            n_1, n_2 = curr, n_1

        return n_1
