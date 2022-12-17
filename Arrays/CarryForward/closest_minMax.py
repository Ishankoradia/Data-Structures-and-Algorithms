"""
Given an array A, find the size of the smallest subarray 
such that it contains at least one occurrence of the maximum value of the array

and at least one occurrence of the minimum value of the array.
"""
def solve(A):
    max_a = A[0]
    for i in range(len(A)):
        if A[i] > max_a:
            max_a = A[i]

    min_a = A[0]
    for i in range(len(A)):
        if A[i] < min_a:
            min_a = A[i]

    max_idx = -1
    min_idx = -1
    ans = len(A)
    for i in range(len(A)):
        if A[i] == max_a:
            if min_idx >= 0 and i - min_idx + 1 < ans:
                ans = i - min_idx + 1
            max_idx = i

        if A[i] == min_a:
            if max_idx >= 0 and i - max_idx + 1 < ans:
                ans = i - max_idx + 1
            min_idx = i

    return ans