"""
https://leetcode.com/problems/length-of-last-word/
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        cnt = 0
        last_word_cnt = 0
        for ch in s:
            if ch == " ":
                if cnt > 0:
                    last_word_cnt = cnt
                cnt = 0
            else:
                cnt += 1

        return cnt if cnt > 0 else last_word_cnt
