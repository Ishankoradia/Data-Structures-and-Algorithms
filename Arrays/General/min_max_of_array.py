"""
Given an array A of size N. You need to find the sum of Maximum and Minimum element in the given array.
"""
def solve( A):
    max_val = A[0]
    for i in range(len(A)):
        if(A[i] > max_val):
            max_val = A[i]

    min_val = A[0]
    for i in range(len(A)):
        if(A[i] < min_val):
            min_val = A[i]

    return max_val + min_val