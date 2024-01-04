"""
You are given a 0-indexed array nums consisting of positive integers.

There are two types of operations that you can apply on the array any number of times:

- Choose two elements with equal values and delete them from the array.
- Choose three elements with equal values and delete them from the array.

Return the minimum number of operations required to make the array empty, or -1 if it is not possible.
"""


def min_operations(nums: list) -> int:
    hm = dict()
    for n in nums:
        hm[n] = hm.get(n, 0) + 1

    ops = 0
    for n in hm.keys():
        if hm[n] % 3 == 0:
            ops += hm[n] // 3
        elif hm[n] % 3 == 1 and hm[n] > 4:
            ops += 2  # subtract 4 (min) to make it multiple of 3
            ops += (hm[n] - 4) // 3
        elif hm[n] % 3 == 2 and hm[n] > 4:
            ops += 1  # subtract 2
            ops += (hm[n] - 2) // 3
        elif hm[n] % 2 == 0:
            ops += hm[n] // 2
        else:
            return -1

    return ops


assert (
    min_operations(
        [14, 12, 14, 14, 12, 14, 14, 12, 12, 12, 12, 14, 14, 12, 14, 14, 14, 12, 12]
    )
    == 7
)
assert (
    min_operations(
        [3, 14, 3, 14, 3, 14, 14, 3, 3, 14, 14, 14, 3, 14, 14, 3, 14, 14, 14, 3]
    )
    == 7
)
assert min_operations([2, 1, 2, 2, 3, 3]) == -1
assert min_operations([2, 3, 3, 2, 2, 4, 2, 3, 4]) == 4
