"""
Given an integer array A of size N. In one second, you can increase the value of one element by 1.

Find the minimum time in seconds to make all elements of the array equal.
"""
def solve( A):
    max_val = A[0]
    for x in A:
        if(x > max_val):
            max_val = x

    secs = 0
    for x in A:
        secs += (max_val - x)

    return secs