"""
Farmer John has built a new long barn with N stalls. 
Given an array of integers A of size N where each element of the array 
represents the location of the stall and an integer B which represents the number of cows.

His cows don't like this barn layout and become aggressive towards each other once put into a stall. 
To prevent the cows from hurting each other, 
John wants to assign the cows to the stalls, 
such that the minimum distance between any two of them is as large as possible. 
What is the largest minimum distance?
"""


def solve(A, B):
    A.sort()
    N = len(A)
    low = 0
    high = A[N - 1]

    def checkMinDistance(arr, B, min_dist):
        # place 1 cow in the beginning
        cows = 0
        prev_dist = arr[0]
        cows += 1
        for i in range(1, len(arr)):
            if (arr[i] - prev_dist) >= min_dist:
                cows += 1
                prev_dist = arr[i]

        return cows >= B

    ans = 0

    while low <= high:
        mid = (low + high) // 2
        if checkMinDistance(A, B, mid):
            low = mid + 1
            ans = mid
        else:
            high = mid - 1

    return ans
