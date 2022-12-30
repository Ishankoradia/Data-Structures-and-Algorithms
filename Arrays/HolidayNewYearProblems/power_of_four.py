'''
Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.
'''
def isPowerOfFour(self, n: int) -> bool:
    return (n & n-1 == 0) and (n-1) % 3 == 0