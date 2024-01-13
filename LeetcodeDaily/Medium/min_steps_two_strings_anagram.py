"""
You are given two strings of the same length s and t. 
In one step you can choose any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.
"""


def minSteps(s: str, t: str) -> int:
    d1 = {}
    for ch in s:  # s
        d1[ch] = d1.get(ch, 0) + 1

    d2 = {}
    for ch in t:  # t
        d2[ch] = d2.get(ch, 0) + 1

    ans = 0
    for ch, cnt in d1.items():
        if ch in d2 and d2[ch] < cnt:
            ans += cnt - d2[ch]

        if ch not in d2:
            ans += cnt

    return ans


assert minSteps("leetcode", "practice") == 5
