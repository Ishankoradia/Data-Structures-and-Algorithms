from Trees.Implement.implementation import TrieBitNode


def build_bit_trie(arr) -> tuple:
    """input is array of number"""

    # max element
    max_ele = max(arr)

    # check how many bits are in the max elements
    temp = max_ele
    max_bit_cnt = 0
    while temp > 0:
        temp = temp >> 1
        max_bit_cnt += 1

    # build
    root = TrieBitNode(0)

    for num in arr:
        curr = root
        for i in range(max_bit_cnt - 1, -1, -1):
            idx = num >> i & 1

            if curr.children[idx] is None:
                curr.children[idx] = TrieBitNode(idx)

            curr = curr.children[idx]

    return (root, max_bit_cnt)


nums = [3, 6, 12, 14]

root, max_bit_cnt = build_bit_trie(nums)

# test cases

# level 1
assert root.children[0] is not None
assert root.children[1] is not None

# level 2
assert root.children[0].children[0] is not None
assert root.children[0].children[1] is not None
assert root.children[1].children[0] is None
assert root.children[1].children[1] is not None

# level 3
assert root.children[0].children[0].children[0] is None
assert root.children[0].children[0].children[1] is not None
assert root.children[0].children[1].children[0] is None
assert root.children[0].children[1].children[1] is not None
assert root.children[1].children[1].children[0] is not None
assert root.children[1].children[1].children[1] is not None

# level 4
assert root.children[0].children[0].children[1].children[1] is not None
assert root.children[0].children[0].children[1].children[0] is None
assert root.children[0].children[1].children[1].children[0] is not None
assert root.children[0].children[1].children[1].children[1] is None
assert root.children[1].children[1].children[0].children[0] is not None
assert root.children[1].children[1].children[0].children[1] is None
assert root.children[1].children[1].children[1].children[0] is not None
assert root.children[1].children[1].children[1].children[1] is None
