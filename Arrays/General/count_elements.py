"""
Given an array A of N integers. Count the number of elements that have at least 1 elements greater than itself.
"""
def solve( A):
    max_val = A[0]
    max_count = 0
    l = len(A)
    # The idea is besides the max element, all elements will have atleast one element greater than itself.
    # We also need to take into account the frequency of the max element
    for i in range(l):

        if(A[i] == max_val):
            max_count += 1

        if(A[i] > max_val):
            max_val = A[i]
            max_count = 1
    
    return l - max_count
