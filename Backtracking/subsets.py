"""
Given a set of distinct integers A, return all possible subsets.
"""
import functools


def subsets(arr):
    global final
    global ans
    ans = []
    final = []

    arr.sort()

    def permute(arr, idx):
        global final
        global ans
        if idx == len(arr):
            final.append(ans.copy())
            return

        # include arr[idx]
        ans.append(arr[idx])
        permute(arr, idx + 1)

        # pop
        ans.pop()

        # exclude arr[idx]
        permute(arr, idx + 1)

    permute(arr, 0)

    def compare(x, y):
        if len(x) > 0 and len(y) > 0:
            min_len = min(len(x), len(y))
            idx = 0
            while idx <= (min_len - 1):
                if x[idx] != y[idx]:
                    break
                idx += 1

            if idx > (min_len - 1):
                idx = min_len - 1

            if x[idx] < y[idx]:
                return -1
            elif x[idx] == y[idx]:
                return -1 if len(x) < len(y) else 1
            else:
                return 1
        elif len(x) == 0:
            return -1
        else:
            return 1

    # final.sort(key=functools.cmp_to_key(compare))

    return sorted(final)


ans = subsets([3, 1, 2])
print(ans)

assert ans[0] == []
assert ans[1] == [1]
assert ans[2] == [1, 2]
assert ans[3] == [1, 2, 3]
assert ans[4] == [1, 3]
assert ans[5] == [2]
assert ans[6] == [2, 3]
assert ans[7] == [3]
