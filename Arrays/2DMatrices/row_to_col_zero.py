"""
You are given a 2D integer matrix A, 
make all the elements in a row or column zero if the A[i][j] = 0. 
Specifically, make entire ith row and jth column zero.
"""
def solve(self, A):
    r = set()
    c = set()
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] == 0:
                r.add(i)
                c.add(j)

    for row in r:
        for j in range(len(A[0])):
            A[row][j] = 0

    for col in c:
        for i in range(len(A)):
            A[i][col] = 0

    return A