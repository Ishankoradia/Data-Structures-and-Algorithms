"""
You are given an array A of integers of size N.

Your task is to find the equilibrium index of the given array

The equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes.

Note:

Array indexing starts from 0.
If there is no equilibrium index then return -1.
If there are more than one equilibrium indexes then return the minimum index.
"""
def solve(self, A):
    for i in range(1,len(A)):
        A[i] = A[i] + A[i-1]

    for i in range(len(A)):
        left = A[i-1] if i > 0 else 0
        right = A[len(A) - 1] - A[i]
        if left == right:
            return i

    return -1