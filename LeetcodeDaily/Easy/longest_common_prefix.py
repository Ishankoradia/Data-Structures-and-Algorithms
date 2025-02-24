"""
https://leetcode.com/problems/longest-common-prefix/description/
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # ans = ""

        # for i in range(200):
        #     prev = None
        #     for word in strs:
        #         if i >= len(word):
        #             return ans

        #         if prev is None:
        #             prev = word[i]
        #         else:
        #             if word[i] != prev:
        #                 return ans

        #     ans += prev

        # return ans

        # another approach
        if not strs:
            return ""

        prefix = strs[0]  # assume the first word is the prefix
        for word in strs[1:]:
            while word.find(prefix) != 0:
                prefix = prefix[
                    :-1
                ]  # take everything except the last char if prefix not found
                if not prefix:
                    return ""

        return prefix
