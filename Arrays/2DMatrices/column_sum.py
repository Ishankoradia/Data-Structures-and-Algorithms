"""
You are given a 2D integer matrix A, return a 1D integer array containing column-wise sums of original matrix.
"""
def solve(self, A):
    r = len(A)
    c = len(A[0])
    col_sum = []
    for j in range(c):
        sum1 = 0
        for i in range(r):
            sum1 += A[i][j]
        col_sum.append(sum1)
    
    return col_sum