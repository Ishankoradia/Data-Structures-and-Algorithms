"""
Given an array of size N, find the subarray of size K with the least average.
"""
def solve(self, A, B):
    start = 0
    end = B - 1
    sum1 = 0
    for i in range(start, end+1):
        sum1 += A[i]

    min_sum1 = sum1
    min_idx = 0

    start += 1
    end += 1
    while end < len(A):
        sum1 = sum1 - A[start - 1] + A[end]

        if (sum1 < min_sum1):
            min_sum1 = sum1
            min_idx = start

        start += 1
        end += 1

    return min_idx

