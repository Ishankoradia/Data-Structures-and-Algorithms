"""
Given an array of integers A, 
find and return the product array of the same size 
where the ith element of the product array will be equal 
to the product of all the elements divided by the ith element of the array.

Note: It is always possible to form the product array with integer (32 bit) values. Solve it without using the division operator.
"""
def solve(self, A):
    p = [1] * len(A)
    for i in range(1, len(A)):
        p[i] = p[i - 1] * A[i-1]

    s = [1] * len(A)
    for i in range(len(A)-2, -1, -1):
        s[i] = s[i + 1] * A[i + 1]

    for i in range(len(A)):
        A[i] = p[i] * s[i]

    return A