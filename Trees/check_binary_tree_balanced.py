"""
A balanced binary tree is defined as
|                                                  |
|  heigh of left subtree - height of right subtree |  <=  1 for all nodes
|                                                  |
"""
from Trees.Implement.implementation import BinaryNode


def is_balanced_tree(root: BinaryNode):
    hm = {"ans": True}

    def height(root: BinaryNode, hm: dict):
        if root is None:
            return -1

        height_lst = height(root.left, hm)
        height_rst = height(root.right, hm)

        if abs(height_lst - height_rst) > 1:
            hm["ans"] = False

        return max(height_rst, height_lst) + 1

    height(root, hm)

    return hm["ans"]


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

assert is_balanced_tree(root) is False
