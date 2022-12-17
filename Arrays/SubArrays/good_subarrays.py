"""
Given an array of integers A, a subarray of an array is said to be good if it fulfills any one of the criteria:
1. Length of the subarray is be even, and the sum of all the elements of the subarray must be less than B.
2. Length of the subarray is be odd, and the sum of all the elements of the subarray must be greater than B.
Your task is to find the count of good subarrays in A.
"""
def solve(self, A, B):
    cnt = 0
    for i in range(len(A)):
        sum1 = 0
        for j in range(i, len(A)):
            sum1 += A[j]
            if((j - i + 1) % 2 == 0  and sum1 < B ) or ((j - i + 1) % 2 != 0  and sum1 > B):
                cnt += 1

    return cnt