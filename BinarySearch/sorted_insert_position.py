"""
You are given a sorted array A of size N and a target value B.
Your task is to find the index (0-based indexing) of the target value in the array.

If the target value is present, return its index.
If the target value is not found, return the index of least element greater than equal to B.
Your solution should have a time complexity of O(log(N)).
"""


def sorted_inserted_pos(A, B):
    low = 0
    high = len(A) - 1

    while low <= high:
        mid = (low + high) // 2

        if A[mid] == B:
            return mid
        elif B < A[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return low
