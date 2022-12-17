"""
You are given a N X N integer matrix. You have to find the sum of all the main diagonal elements of A.
"""
def solve(self, A):
    r = len(A)
    c = len(A[0])
    sum1 = 0
    i = 0
    j = 0
    while i < r and j < c:
        sum1 +=  A[i][j]
        i += 1
        j += 1

    return sum1