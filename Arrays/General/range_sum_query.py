"""
You are given an integer array A of length N.
You are also given a 2D integer array B with dimensions M x 2, where each row denotes a [L, R] query.
For each query, you have to find the sum of all elements from L to R indices in A (1 - indexed).
More formally, find A[L] + A[L + 1] + A[L + 2] +... + A[R - 1] + A[R] for each query.
"""
def solve( A, B):
    for j, query in enumerate(B):
        L = query[0] - 1
        R = query[1]
        sum1 = 0
        for i in range(L, R):
            sum1 += A[i]

        B[j] = sum1

    return B