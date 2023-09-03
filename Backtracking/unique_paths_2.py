def unique_path(A):
    """unique paths"""
    global count
    global zeros
    count = 0

    N = len(A)
    M = len(A[0])

    start_i = 0
    start_j = 0
    zeros = 0
    for i in range(N):
        for j in range(M):
            if A[i][j] == 1:
                start_i = i
                start_j = j

            if A[i][j] == 0:
                zeros += 1

    def visit(arr, i, j, cnt):
        global count
        global zeros

        A[i][j] = 3  # visited

        #    [r, t, l, b]
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        # pylint: disable=consider-using-enumerate
        # for each direction
        for ii in range(len(dx)):
            ni = i + dx[ii]
            nj = j + dy[ii]

            if ni >= 0 and ni < N and nj >= 0 and nj < M:
                if A[ni][nj] == 0:
                    visit(arr, ni, nj, cnt + 1)

                if A[ni][nj] == 2:
                    if cnt == zeros:
                        count += 1

        A[i][j] = 0

    visit(A, start_i, start_j, 0)

    return count


assert unique_path([[1, 0], [0, 2]]) == 0
assert unique_path([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]) == 2
