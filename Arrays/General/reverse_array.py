"""
You are given a constant array A.

You are required to return another array which is the reversed form of the input array.
"""
def solve( A):       
    A1 = [i for i in A]
    i = 0
    j = len(A1) - 1
    while i < j:
        temp = A1[i]
        A1[i] = A1[j]
        A1[j] = temp
        i+=1
        j-=1

    return A1