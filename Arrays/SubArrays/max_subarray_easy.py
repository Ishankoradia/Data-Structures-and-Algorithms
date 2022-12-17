"""
You are given an integer array C of size A. 
Now you need to find a subarray (contiguous elements) so that the sum of contiguous elements is maximum.
But the sum must not exceed B.
"""
def maxSubarray(self, A, B, C):
    max_sum = None
    for i in range(A):
        sum1 = 0
        for j in range(i, A):
            sum1 = sum1 + C[j]
            max_sum = sum1 if (max_sum is None or sum1 > max_sum) and sum1 <= B else max_sum

    return max_sum if max_sum else 0