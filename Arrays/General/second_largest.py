"""
You are given an integer array A. You have to find the second largest element/value in the array or report that no such element exists.
"""
def solve( A):
    max_val = -1
    for i in A:
        if i > max_val:
            max_val = i

    second_max = -1
    for i in A:
        if i > second_max and i != max_val:
            second_max = i

    return second_max