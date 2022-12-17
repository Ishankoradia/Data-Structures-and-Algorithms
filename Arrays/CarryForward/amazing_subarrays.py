"""
You are given a string S, and you have to find all the amazing substrings of S.

An amazing Substring is one that starts with a vowel (a, e, i, o, u, A, E, I, O, U).

Return a single integer X mod 10003, here X is the number of Amazing Substrings in given the string.
"""
def solve(self, A):
    vowels = ['a', 'e', 'i', 'o', 'u']
    cnt = 0
    for i in range(len(A)):
        if A[i].lower() in vowels:
            cnt+= (len(A) - i)

    return cnt % 10003