"""
You are given a matrix A, you have to return another matrix which is the transpose of A.
"""
def solve(self, A):
    B = [[0 for _ in range(len(A))] for _ in range(len(A[0])) ]
    for i in range(len(A)):
        for j in range(len(A[0])):
            B[j][i] = A[i][j]

    return B