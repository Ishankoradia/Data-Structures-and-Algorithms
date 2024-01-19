"""
Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row 
that is either directly below or diagonally left/right. 
Specifically, the next element from position (row, col) will be 
(row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

Input: matrix = [[-19,57],[-40,-5]]
Output: -59

Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 100
-100 <= matrix[i][j] <= 100
"""


def minFallingPathSum(matrix) -> int:
    global N
    N = len(matrix)  # rows & columns ; square matrix

    dp = [[10**5] * N for _ in range(N)]
    # dp[i][j] is the minimum sum falling path ending at i,j

    def traverseFalling(i, j, mat):
        global N
        if i < 0:
            return 0

        if dp[i][j] != 10**5:
            return dp[i][j]

        f = min(dp[i][j], mat[i][j] + traverseFalling(i - 1, j, mat))

        if j - 1 >= 0:
            f = min(f, mat[i][j] + traverseFalling(i - 1, j - 1, mat))

        if j + 1 < N:
            f = min(f, mat[i][j] + traverseFalling(i - 1, j + 1, mat))

        dp[i][j] = f

        return dp[i][j]

    ans = 10**5  # based on constraints
    for j in range(N):  # start with the possibilities where the falling path can end
        ans = min(ans, traverseFalling(N - 1, j, matrix))

    return ans


assert minFallingPathSum([[-19, 57], [-40, -5]]) == -59
assert minFallingPathSum([[2, 1, 3], [6, 5, 4], [7, 8, 9]]) == 13
