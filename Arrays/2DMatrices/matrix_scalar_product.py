"""
You are given a matrix A and and an integer B,
you have to perform scalar multiplication of matrix A with an integer B.
"""
def solve(self, A, B):
    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i][j] = B * A[i][j]

    return A