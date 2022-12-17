"""
Given an integer array A containing N distinct integers, you have to find all the leaders in array A.

An element is a leader if it is strictly greater than all the elements to its right side.

Note:The rightmost element is always a leader.
"""
def solve(self, A):
    ans = [A[-1]]
    max_ele = A[-1]
    for i in range(len(A)-2, -1, -1):
        if(A[i] > max_ele):
            max_ele = A[i]
            ans.append(A[i])

    return ans