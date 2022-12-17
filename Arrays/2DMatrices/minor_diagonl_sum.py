"""
You are given a N X N integer matrix. 
You have to find the sum of all the minor diagonal elements of A.

Minor diagonal of a M X M matrix A is a collection of elements A[i, j] such that i + j = M + 1 (where i, j are 1-based).
"""
def solve(self, A):
    c = len(A[0])
    i = 0
    j = c - 1
    sum1 = 0
    while i < c and j >= 0:
        sum1 += A[i][j]
        i += 1
        j -= 1

    return sum1