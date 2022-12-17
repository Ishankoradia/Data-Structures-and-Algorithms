"""
Given an integer A, 
generate a square matrix filled with elements from 1 to A2 in spiral order 
and return the generated square matrix.
"""
def generateMatrix(self, A):
    B = [[0 for _ in range(A)] for _ in range(A)]
    N = A
    num = 1
    i = 0
    j = 0
    while (N > 1):
        for k in range(1, N):
            B[i][j] = num
            num += 1
            j += 1

        for k in range(1, N):
            B[i][j] = num
            num += 1
            i += 1

        for k in range(1, N):
            B[i][j] = num
            num += 1
            j -= 1

        for k in range(1, N):
            B[i][j] = num
            num += 1
            i -= 1

        N = N - 2
        i += 1
        j += 1

    if(N == 1):
        B[i][j] = num

    return B
