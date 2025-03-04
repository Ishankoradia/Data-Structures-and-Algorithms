"""
https://leetcode.com/problems/sqrtx/description/
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        # i = 0
        # ans = 0
        # while  i * i <= x:
        #     ans = i
        #     i += 1

        # return ans

        # using binary search

        if x == 0 or x == 1:
            return x

        start = 1
        end = x
        while start <= end:
            mid = (start + end) // 2
            if mid * mid <= x and (mid + 1) ** 2 > x:
                return mid
            elif mid * mid < x:
                start = mid + 1
            else:
                end = mid - 1
