"""
Given an integer array A of size N and an integer B, 
you have to return the same array after rotating it B times towards the right.
"""
def solve( A, B):
    def reverse(A, start, stop):
        i = start
        j = stop
        while i < j:
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
            i+=1
            j-=1

    n = len(A)

    B = B % n

    reverse(A, 0, n-1)
    reverse(A, B, n-1)
    reverse(A, 0, B-1)

    return A

print(solve([1,2,3,4,5], 2))