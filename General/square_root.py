"""
Given a number A. Return square root of the number if it is perfect square otherwise return -1.
"""
def solve( A):
    i = 1
    cnt = 0
    while i * i <= A:
        if(A % i == 0 and i == A / i):
            return i
        i += 1

    return -1