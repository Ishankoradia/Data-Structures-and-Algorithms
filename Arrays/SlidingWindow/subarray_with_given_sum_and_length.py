"""
Given an array A of length N. Also given are integers B and C.

Return 1 if there exists a subarray with length B having sum C and 0 otherwise
"""
def solve(self, A, B, C):
    start = 0
    end = B - 1
    sum1 = 0
    for i in range(B):
        sum1 = sum1 + A[i]

    if(sum1 == C):
        return 1

    start += 1
    end += 1
    while end < len(A):
        sum1 = sum1 - A[start - 1] + A[end]
        if(sum1 == C):
            return 1

        start += 1
        end += 1

    return 0