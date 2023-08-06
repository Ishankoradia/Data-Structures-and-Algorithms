from Trees.Implement.implementation import BinaryNode


def lca_bst(root: BinaryNode, k1: int, k2: int):
    if k1 == k2:
        return k1
    curr = root
    while curr is not None:
        if k1 > curr.val and k2 > curr.val:
            curr = curr.right
        elif k1 < curr.val and k2 < curr.val:
            curr = curr.left
        else:
            return curr.val


# test cases

# level 1
root = BinaryNode(10)

# level 2
root.left = BinaryNode(7)
root.right = BinaryNode(20)

# level 3
root.left.right = BinaryNode(3)
root.right.left = BinaryNode(17)
root.right.right = BinaryNode(23)

# level 4
root.right.left.right = BinaryNode(16)
root.right.right.left = BinaryNode(24)
root.right.right.right = BinaryNode(25)

assert lca_bst(root, 16, 24) == 20
assert lca_bst(root, 17, 23) == 20
assert lca_bst(root, 24, 24) == 24
assert lca_bst(root, 3, 25) == 10
