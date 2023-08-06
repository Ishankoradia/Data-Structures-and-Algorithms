from Trees.Implement.implementation import BinaryNode


def search_bt(root: BinaryNode, k: int):
    if root is None:
        return False

    if root.val == k:
        return True

    if search_bt(root.left, k) is True:
        return True

    if search_bt(root.right, k) is True:
        return True

    return False


# create the tree
root = BinaryNode(5)
# level 1
root.left = BinaryNode(12)
root.right = BinaryNode(6)

# level 2
root.left.right = BinaryNode(9)
root.right.left = BinaryNode(-1)
root.right.right = BinaryNode(10)

# level 3
root.right.right.left = BinaryNode(9)
root.left.right.left = BinaryNode(4)
root.left.right.right = BinaryNode(15)

# level 4
root.right.right.left.left = BinaryNode(19)


assert search_bt(root, 9) is True
assert search_bt(root, -1) is True
assert search_bt(root, 4) is True
assert search_bt(root, 15) is True
assert search_bt(root, 19) is True

assert search_bt(root, 100) is False
assert search_bt(root, -100) is False
