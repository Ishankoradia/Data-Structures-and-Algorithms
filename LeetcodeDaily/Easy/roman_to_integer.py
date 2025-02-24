"""
https://leetcode.com/problems/roman-to-integer/description/
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        # num = 0
        # i = 0
        # while i < len(s):
        #     curr_i = i
        #     if s[i] == 'I':
        #         if i+1 < len(s):
        #             if s[i+1] == 'V':
        #                 num += 4
        #                 i += 2
        #             elif s[i+1] == 'X':
        #                 num += 9
        #                 i += 2
        #     elif s[i] == 'X':
        #         if i+1 < len(s):
        #             if s[i+1] == 'L':
        #                 num += 40
        #                 i += 2
        #             elif s[i+1] == 'C':
        #                 num += 90
        #                 i += 2
        #     elif s[i] == 'C':
        #         if i+1 < len(s):
        #             if s[i+1] == 'D':
        #                 num += 400
        #                 i += 2
        #             elif s[i+1] == 'M':
        #                 num += 900
        #                 i += 2
        #     if curr_i == i:
        #         num += hashmap[s[i]]
        #         i += 1

        # return num

        # a clean better approach
        # i = 0
        # num = 0
        # while i < len(s):
        #     if (i + 1) < len(s):
        #         if hashmap[s[i]] >= hashmap[s[i+1]]:
        #             num += hashmap[s[i]]
        #         else:
        #             num -= hashmap[s[i]]
        #     else:
        #         num += hashmap[s[i]]
        #     i += 1

        # return num

        # using zip - different approach
        num = 0
        for a, b in zip(s, s[1:]):
            if hashmap[a] < hashmap[b]:
                num -= hashmap[a]
            else:
                num += hashmap[a]

        return num + hashmap[s[-1]]
