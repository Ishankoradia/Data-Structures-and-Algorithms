"""
Given an array of integers A. 
If i < j and A[i] > A[j], then the pair (i, j) is called an inversion of A. 
Find the total number of inversions of A modulo (10**9 + 7).
"""


def merge(arr, s, mid, e):
    temp = [0 for _ in range(e - s + 1)]
    inv_cnt = 0

    p1 = s
    p2 = mid + 1
    p3 = 0
    while p1 <= mid and p2 <= e:
        if arr[p1] <= arr[p2]:
            temp[p3] = arr[p1]
            p1 += 1
        else:
            temp[p3] = arr[p2]
            p2 += 1
            inv_cnt += mid - p1 + 1
        p3 += 1

    while p1 <= mid:
        temp[p3] = arr[p1]
        p1 += 1
        p3 += 1

    while p2 <= e:
        temp[p3] = arr[p2]
        p2 += 1
        p3 += 1

    for i in range(s, e + 1):
        arr[i] = temp[i - s]

    return inv_cnt


def merge_sort(A, s, e):
    if s == e:
        return 0

    mid = (s + e) // 2

    inv_left = merge_sort(A, s, mid)
    inv_right = merge_sort(A, mid + 1, e)
    inv = merge(A, s, mid, e)

    return (inv + inv_left + inv_right) % (10**9 + 7)


def inversion_pairs(A):
    return merge_sort(A, 0, len(A) - 1) % (10**9 + 7)


assert inversion_pairs([3, 4, 1, 2]) == 4
