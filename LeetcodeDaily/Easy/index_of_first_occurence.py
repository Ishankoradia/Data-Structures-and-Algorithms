"""
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        j = 0
        idx = -1
        while i < len(haystack):
            idx = i
            while i < len(haystack) and j < len(needle) and haystack[i] == needle[j]:
                i += 1
                j += 1

            if j == len(needle):
                return idx

            # didn't get the match, reset
            i = idx + 1
            j = 0
            idx = -1

        return idx
