"""
Given an array of integers A and an integer B, 
find and return the minimum number of swaps required to bring all the numbers less than or equal to B together.

Note: It is possible to swap any two elements, not necessarily consecutive.
"""
def solve(self, A, B):
    k = 0
    for i in range(len(A)):
        if A[i] <= B:
            k += 1

    if k == 0 or k == 1 or k == len(A):
        return 0

    start = 0
    end = k - 1

    sum_cnt = 0
    for i in range(end+1):
        if A[i] <= B:
            sum_cnt += 1

    start += 1
    end += 1

    max_cnt = sum_cnt

    while end < len(A):
        if A[start-1] <= B:
            sum_cnt -= 1

        if A[end] <= B:
            sum_cnt += 1

        if sum_cnt > max_cnt:
            max_cnt = sum_cnt

        start += 1
        end += 1

    return k - max_cnt