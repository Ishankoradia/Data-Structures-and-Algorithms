"""
Given an array A of N integers. 
Also given are two integers B and C. 
Reverse the array A in the given range [B, C]
"""
def solve( A, B, C):
    i = B
    j = C
    while i < j:
        temp = A[i]
        A[i] = A[j]
        A[j] = temp
        i+=1
        j-=1

    return A