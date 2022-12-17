"""
You are given an integer array A of length N.
You are also given a 2D integer array B with dimensions M x 2, where each row denotes a [L, R] query.
For each query, you have to find the sum of all elements from L to R indices in A (1 - indexed).
More formally, find A[L] + A[L + 1] + A[L + 2] +... + A[R - 1] + A[R] for each query.
"""
def rangeSum(A, B):
    pf = [0] * len(A)
    pf[0] = A[0]
    for i in range(1, len(A)):
        pf[i] = pf[i-1] + A[i]
    
    for i, q in enumerate(B):
        L = q[0]-1
        R = q[1]-1
        if L == 0:
            B[i] = pf[R]
        else:
            B[i] = pf[R] - pf[L - 1]

    return B