"""
Find the Bth smallest element in given array A .

NOTE: Users should try to solve it in less than equal to B swaps.
"""


def kthsmallest_selection_sort(A, B):
    N = len(A)

    for i in range(N):
        min_ele = A[i]

        idx = i
        for j in range(i, N):
            if A[j] < min_ele:
                idx = j
                min_ele = A[j]

        # swap i, idx
        temp = A[i]
        A[i] = A[idx]
        A[idx] = temp

        if i == B - 1:
            return A[i]


arr = [4, 23, 1, 7, 10, 2]
assert kthsmallest_selection_sort(arr, 1) == 1
assert kthsmallest_selection_sort(arr, 2) == 2
assert kthsmallest_selection_sort(arr, 3) == 4
assert kthsmallest_selection_sort(arr, 4) == 7


def kthsmallest_bubble_sort(A, B):
    N = len(A)

    for i in range(N):
        for j in range(N - i - 1):
            if A[j] < A[j + 1]:
                # swap
                temp = A[j + 1]
                A[j + 1] = A[j]
                A[j] = temp

        if i == B - 1:
            return A[N - i - 1]


arr = [4, 23, 1, 7, 10, 2]
assert kthsmallest_bubble_sort(arr, 1) == 1
assert kthsmallest_bubble_sort(arr, 2) == 2
assert kthsmallest_bubble_sort(arr, 3) == 4
assert kthsmallest_bubble_sort(arr, 4) == 7
