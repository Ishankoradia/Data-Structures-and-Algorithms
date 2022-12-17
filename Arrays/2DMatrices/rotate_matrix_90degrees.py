"""
You are given a n x n 2D matrix A representing an image.

Rotate the image by 90 degrees (clockwise).

You need to do this in place.
"""
def solve(self, A):
    for i in range(len(A)):
        for j in range(i+1, len(A[0])):
            temp = A[i][j]
            A[i][j] = A[j][i]
            A[j][i] = temp

        p1 = 0
        p2 = len(A) - 1
        while p1 < p2:
            temp = A[i][p1]
            A[i][p1] = A[i][p2]
            A[i][p2] = temp
            p1 += 1
            p2 -= 1

    return A