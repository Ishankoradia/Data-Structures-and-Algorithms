"""
You are given an integer array A of size N.

You have to pick B elements in total. 
Some (possibly 0) elements from left end of array A and 
some (possibly 0) from the right end of array A to get the maximum sum.

Find and return this maximum possible sum.

Note: Suppose B = 4, and array A contains 10 elements, then

You can pick the first four elements or can pick the last four elements, 
or can pick 1 from front and 3 from the back, etc. 
You need to return the maximum possible sum of elements you can pick.
"""
def solve(self, A, B):
    pf = [0] * len(A)
    pf[0] = A[0]
    for i in range(1, len(A)):
        pf[i] = pf[i-1] + A[i]

    sf = [0] * len(A)
    sf[len(A)-1] = A[len(A) - 1]
    for i in range(len(A)-2, -1, -1):
        sf[i] = sf[i+1] + A[i]

    i = 0
    n = len(A)
    j = len(A) - 1
    k = B
    ans = None
    while k > -1:
        left_s = pf[k - 1] if k > 0 else 0
        right_s = sf[len(A) - (B - k - 1) - 1] if k - B < 0 else 0

        ans = left_s + right_s if ans is None or left_s + right_s > ans else ans

        k -= 1

    return ans 