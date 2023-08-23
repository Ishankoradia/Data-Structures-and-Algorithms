"""Flatten binary tree to linked list"""
from Trees.Implement.implementation import BinaryNode
from Trees.Traversals.inorder import inorder_recursive


def flatten(root: BinaryNode):
    """Function"""
    if root is None:
        return

    flatten(root.left)
    flatten(root.right)

    k = root.right
    if root.left is not None:
        root.right = root.left
        root.left = None

        temp = root.right
        while temp.right is not None:
            temp = temp.right

        temp.right = k


root = BinaryNode(100)

# level 1
root.left = BinaryNode(2)
root.right = BinaryNode(7)

# level 2
root.left.left = BinaryNode(3)
root.left.right = BinaryNode(4)
root.right.left = BinaryNode(8)
root.right.right = BinaryNode(9)

# level 3
root.left.right.left = BinaryNode(5)
root.left.right.right = BinaryNode(6)
root.right.right.right = BinaryNode(10)

flatten(root)

assert inorder_recursive(root, []) == [100, 2, 3, 4, 5, 6, 7, 8, 9, 10]
