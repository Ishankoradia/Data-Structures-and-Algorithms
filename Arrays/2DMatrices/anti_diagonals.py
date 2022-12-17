"""
Give a N * N square matrix A, return an array of its anti-diagonals. Look at the example for more details.
"""
def diagonal(self, A):
    N = len(A)
    ans = [[0 for i in range(N)] for j in range(2*N-1)]
    r = 0
    for y in range(N):
        i = 0
        j = y
        c = 0
        while (i < N and j >= 0):
            ans[r][c] = A[i][j]
            i += 1
            j -= 1
            c += 1
        r += 1

    for x in range(1, N):
        i = x
        j = N - 1
        c = 0
        while (i < N and j >= 0):
            ans[r][c] = A[i][j]
            i += 1
            j -= 1
            c += 1
        r += 1

    return ans