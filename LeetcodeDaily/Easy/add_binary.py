"""
https://leetcode.com/problems/add-binary/description/
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # num1 = 0
        # mul = 0
        # for i in range(len(a)-1, -1, -1):
        #     num1 += (int(a[i]) * (2**mul))
        #     mul += 1

        # num2 = 0
        # mul = 0
        # for i in range(len(b)-1, -1, -1):
        #     num2 += (int(b[i]) * (2**mul))
        #     mul += 1

        # ans = num1 + num2
        # ans_bin = ""
        # while ans > 0:
        #     ans_bin = str(ans % 2) + ans_bin
        #     ans = ans // 2

        # return "0" if not ans_bin else ans_bin

        # better optimized way of doing it

        ans = []
        carry = 0
        i = len(a) - 1
        j = len(b) - 1
        while i >= 0 or j >= 0 or carry > 0:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1
            ans.append(str(carry % 2))
            carry = carry // 2

        return "".join(reversed(ans))
