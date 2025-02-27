"""
https://leetcode.com/problems/valid-parentheses/
"""


class Solution:
    def is_valid_pair(self, ch1: str, ch2: str):
        return (
            (ch1 == "(" and ch2 == ")")
            or (ch1 == "[" and ch2 == "]")
            or (ch1 == "{" and ch2 == "}")
        )

    def isValid(self, s: str) -> bool:
        stack = list()
        i = 0
        while i < len(s):
            curr = s[i]
            if len(stack) > 0 and self.is_valid_pair(stack[-1], curr):
                stack.pop()
            else:
                stack.append(curr)

            i += 1

        return len(stack) == 0
