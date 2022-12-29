'''
Given a string s, return true if a permutation of the string could form a 
palindrome and false otherwise.
'''
# Approach 1
def canPermutePalindrome(self, s: str) -> bool:
    d = {}
    for i in s:
        val = d.get(i)
        d[i] = val + 1 if val is not None else 1

    cnt_odd = 0
    for k in d.keys():
        if len(s) % 2 == 0:
            if d[k] % 2 != 0:
                return False
        else:
            if d[k] % 2 != 0:
                cnt_odd += 1

            if cnt_odd > 1:
                return False

    return True

# Approach 2

