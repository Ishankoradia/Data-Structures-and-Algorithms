"""
You are given an integer array A.

Decide whether it is possible to divide the array into one or more subarrays of even length 
such that the first and last element of all subarrays will be even.

Return "YES" if it is possible; otherwise, return "NO" (without quotes).
"""
def solve(self, A):

    if len(A) % 2 != 0 or A[0] % 2 != 0 or A[-1] % 2 != 0:
        return 'NO'

    return 'YES'