"""
Merge sort algo

TC: O(nlogn)
SC: O(n)
"""


def merge(arr, s, mid, e):
    temp = [0 for _ in range(e - s + 1)]

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


def merge_sort(A, s, e):
    if s == e:
        return

    mid = (s + e) // 2
    merge_sort(A, s, mid)
    merge_sort(A, mid + 1, e)
    merge(A, s, mid, e)


def sorting_merge(A):
    merge_sort(A, 0, len(A) - 1)

    return A


arr = [4, 3, 1, 10, -1]
assert sorting_merge(arr) == sorted(arr)
arr = [1]
assert sorting_merge(arr) == sorted(arr)
arr = [3, 2, 1]
assert sorting_merge(arr) == sorted(arr)
