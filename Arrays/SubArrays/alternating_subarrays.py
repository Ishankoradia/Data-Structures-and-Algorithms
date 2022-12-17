"""
You are given an integer array A of length N comprising of 0's & 1's, and an integer B.

You have to tell all the indices of array A that can act as a center of 2 * B + 1 length 0-1 alternating subarray.

A 0-1 alternating array is an array containing only 0's & 1's, and having no adjacent 0's or 1's. 
For e.g. arrays [0, 1, 0, 1], [1, 0] and [1] are 0-1 alternating, while [1, 1] and [0, 1, 0, 0, 1] are not.
"""
def solve(self, A, B):
    ans = []
    for i in range(len(A)):
        start = i - B
        end = i + B
        if(start < 0 or end > len(A)-1):
            continue

        alternate = True
        num = A[start]
        for j in range(start + 1, end + 1):
            if(num ^ A[j]):
                num = A[j]
            else:
                alternate = False
                break

        if(alternate):
            ans.append(i)              

    return ans