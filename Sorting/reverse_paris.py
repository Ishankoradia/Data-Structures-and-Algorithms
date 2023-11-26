"""
Given an integer array nums, return the number of reverse pairs in the array.

A reverse pair is a pair (i, j) where:

- 0 <= i < j < nums.length and
- nums[i] > 2 * nums[j].

"""


def reverse_pairs(nums):
    def merge(arr, s, m, e):
        temp = [0 for _ in range(e - s + 1)]
        p1 = s
        p2 = m + 1
        p3 = 0
        cnt = 0

        while p1 <= m and p2 <= e:
            if arr[p1] > 2 * arr[p2]:
                cnt = cnt + (m - p1 + 1)
                p2 += 1
            else:
                p1 += 1

        p1 = s
        p2 = m + 1
        p3 = 0

        while p1 <= m and p2 <= e:
            if arr[p1] < arr[p2]:
                temp[p3] = arr[p1]
                p1 += 1
                p3 += 1
            else:
                temp[p3] = arr[p2]
                p2 += 1
                p3 += 1

        while p1 <= m:
            temp[p3] = arr[p1]
            p1 += 1
            p3 += 1

        while p2 <= e:
            temp[p3] = arr[p2]
            p2 += 1
            p3 += 1

        for i in range(s, e + 1):
            arr[i] = temp[i - s]

        return cnt

    def merge_sort(arr, s, e):
        if s == e:
            return 0

        mid = (s + e) // 2

        left_cnt = merge_sort(arr, s, mid)
        right_cnt = merge_sort(arr, mid + 1, e)
        cnt = merge(arr, s, mid, e)

        return cnt + left_cnt + right_cnt

    return merge_sort(nums, 0, len(nums) - 1)
