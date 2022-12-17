"""
You are given a 2D integer matrix A, return a 1D integer array containing row-wise sums of original matrix.
"""
def solve(self, A):
    r = len(A)
    c = len(A[0])
    row_sum = []
    for i in range(r):
        sum1 = 0
        for j in range(c):
            sum1 += A[i][j]
        row_sum.append(sum1)

    return row_sum