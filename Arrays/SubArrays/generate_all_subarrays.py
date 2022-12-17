"""
You are given an array A of N integers.
Return a 2D array consisting of all the subarrays of the array
"""
def solve(self, A):
    ans = []
    for i in range(len(A)):
        for j in range(i, len(A)):
            ans.append(A[i: j+1])

    return ans