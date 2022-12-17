"""
Given an array A and an integer B, find the number of occurrences of B in A.
"""
def solve( A, B):
    cnt = 0
    for i in range(len(A)):
        if(A[i] == B):
            cnt += 1

    return cnt