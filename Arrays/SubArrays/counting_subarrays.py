"""
Given an array A of N non-negative numbers and a non-negative number B,
you need to find the number of subarrays in A with a sum less than B.
We may assume that there is no overflow.
"""
def solve(self, A, B):
    cnt = 0
    for i in range(len(A)):
        sum1 = 0
        for j in range(i, len(A)):
            sum1 += A[j]
            if sum1 < B:
                cnt += 1

    return cnt