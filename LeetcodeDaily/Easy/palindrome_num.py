"""
https://leetcode.com/problems/palindrome-number/description/
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # bruteforce (converting to string)
        # num_str = str(x) # takes O(digits * digits)
        # p1 = 0
        # p2 = len(num_str) - 1
        # while p1 < p2:
        #     if num_str[p1] != num_str[p2]:
        #         return False
        #     p1 += 1
        #     p2 -= 1

        # return True

        # optimized approach
        # if x < 0:
        #     return False

        # digits = []
        # while x > 0:
        #     digits.append(x % 10)
        #     x = x // 10

        # p1 = 0
        # p2 = len(digits) - 1
        # while p1 < p2:
        #     if digits[p1] != digits[p2]:
        #         return False
        #     p1 += 1
        #     p2 -= 1

        # return True

        # optimized approach - 2
        if x < 0:
            return False

        reverse = 0
        xcopy = x
        while x > 0:
            reverse = (reverse * 10) + (x % 10)
            x = x // 10

        return xcopy == reverse
