"""
You are given an integer array A of length N.
You have to find the sum of all subarray sums of A.
More formally, a subarray is defined as a contiguous part of an array which we can obtain by deleting zero or more elements from either end of the array.
A subarray sum denotes the sum of all the elements of that subarray.
"""
def subarraySum(self, A):
    # contribution of each element in the net sum is (i+1) * (n-1)
    total_sum = 0
    for i in range(len(A)):
        total_sum += A[i] * ((i+1) * (len(A) - i))

    return total_sum 