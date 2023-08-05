from Trees.Implement.implementation import BinaryNode


def search_bst(root: BinaryNode, k: int):
    if root is None:
        return False

    if root.val == k:
        return True

    if k < root.val:
        return search_bst(root.left, k)
    else:
        return search_bst(root.right, k)


# test cases

# create the tree
root = BinaryNode(15)

# level 1
root.left = BinaryNode(10)
root.right = BinaryNode(21)

# level 2
root.left.left = BinaryNode(5)
root.right.right = BinaryNode(27)

# level 3
root.left.left.left = BinaryNode(1)
root.left.left.right = BinaryNode(8)
root.right.right.left = BinaryNode(24)
root.right.right.right = BinaryNode(34)

assert search_bst(root, 21) is True
assert search_bst(root, 34) is True
assert search_bst(root, 1) is True
assert search_bst(root, 10) is True

assert search_bst(root, 100) is False
assert search_bst(root, -1) is False
