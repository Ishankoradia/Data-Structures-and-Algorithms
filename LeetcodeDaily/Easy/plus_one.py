"""
https://leetcode.com/problems/plus-one/description/
"""

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            sum1 = digits[i] + carry
            digits[i] = sum1 % 10
            carry = sum1 // 10

        if carry > 0:
            return [carry] + digits
        else:
            return digits
