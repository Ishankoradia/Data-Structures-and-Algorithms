"""
Given an array A of N integers. Construct prefix sum of the array in the given array itself.
"""
def solve(self, A):
    for i in range(1, len(A)):
        A[i] = A[i] + A[i-1]

    return A