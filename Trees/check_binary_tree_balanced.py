"""
A balanced binary tree is defined as
|                                                  |
|  heigh of left subtree - height of right subtree |  <=  1 for all nodes
|                                                  |
"""
from Trees.Implement.implementation import BinaryNode


def height(root: BinaryNode, is_balanced: bool = True):
    if root is None:
        return [-1, True]

    height_lst = height(root.left, is_balanced)[0]
    height_rst = height(root.right, is_balanced)[0]

    return [max(height_rst, height_lst) + 1, abs(height_lst - height_rst) <= 1]


# test cases

# create the tree
root = BinaryNode(1)
# level 1
root.left = BinaryNode(2)
root.right = BinaryNode(3)

# level 2
root.left.left = BinaryNode(4)
root.left.right = BinaryNode(3)

# level 3
root.left.left.left = BinaryNode(6)

assert height(root)[0] == 3
assert height(root)[1] == False
