"""
Given a 2D binary matrix of integers A containing 0's and 1's of size N x M.

Find the largest rectangle containing only 1's and return its area.

Note: Rows are numbered from top to bottom and columns are numbered from left to right.
"""
from Stacks.largest_rectangle_historgram import largest_rectangle_hist


def solve(A):
    N = len(A)
    M = len(A[0])

    max_area = largest_rectangle_hist(A[0])
    temp = A[0]
    for i in range(1, N):
        for j in range(M):
            if A[i][j] == 1:
                temp[j] = 1 + temp[j]
            else:
                temp[j] = 0

        max_area = max(max_area, largest_rectangle_hist(temp))

    return max_area


assert solve([[0, 0, 1], [0, 1, 1], [1, 1, 1]]) == 4
