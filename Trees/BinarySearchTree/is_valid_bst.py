from Trees.Implement.implementation import BinaryNode

inf = 10**8


def is_valid_bst(root: BinaryNode, lower: int = -inf, upper: int = inf) -> bool:
    if root is None:
        return True

    if root.val > upper or root.val < lower:
        return False

    is_lst_valid = is_valid_bst(root.left, lower, root.val - 1)

    if is_lst_valid is False:
        return False

    is_rst_valid = is_valid_bst(root.right, root.val + 1, upper)

    if is_rst_valid is False:
        return False

    return True


# test cases

# create the tree
root = BinaryNode(10)

# level 1
root.left = BinaryNode(5)
root.right = BinaryNode(15)

# level 2
root.left.left = BinaryNode(4)
root.left.right = BinaryNode(9)
root.right.left = BinaryNode(13)
root.right.right = BinaryNode(20)

# level 3
root.left.right.left = BinaryNode(7)
root.right.left.right = BinaryNode(14)
root.right.right.left = BinaryNode(9)

assert is_valid_bst(root) is False
root.right.right.left = BinaryNode(17)
assert is_valid_bst(root) is True
