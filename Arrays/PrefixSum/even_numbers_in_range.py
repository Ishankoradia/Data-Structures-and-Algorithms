"""
You are given an array A of length N and Q queries given by the 2D array B of size Q*2.
Each query consists of two integers B[i][0] and B[i][1].
For every query, the task is to find the count of even numbers in the range A[B[i][0]…B[i][1]].
"""
def solve(self, A, B):
    for i in range(len(A)):
        A[i] = 1 if A[i] % 2 == 0 else 0

    for i in range(1, len(A)):
        A[i] = A[i] + A[i-1]

    for i, q in enumerate(B):
        L = q[0]
        R = q[1]
        if L == 0:
            B[i] = A[R]
        else:
            B[i] = A[R] - A[L-1]

    return B