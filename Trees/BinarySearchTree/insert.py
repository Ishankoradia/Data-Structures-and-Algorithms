from Trees.Implement.implementation import BinaryNode
from Trees.BinarySearchTree.search import search_bst


def insert_bst(root: BinaryNode, k: int) -> BinaryNode:
    if root is None:
        nn = BinaryNode(k)
        return nn

    if k <= root.val:
        root.left = insert_bst(root.left, k)
    else:
        root.right = insert_bst(root.right, k)

    return root


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


insert_bst(root, 12)
assert search_bst(root, 12) is True
insert_bst(root, 27)
assert search_bst(root, 27) is True
assert search_bst(root, 100) is False
