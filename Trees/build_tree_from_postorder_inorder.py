"""
Given the inorder and postorder traversal of a tree, construct the binary tree.

NOTE: You may assume that duplicates do not exist in the tree.
"""
from Trees.Implement.implementation import BinaryNode


def buildTree(A, B):
    def find(arr, s, e, val):
        for i in range(s, e + 1):
            if arr[i] == val:
                return i

    def build(inord, s1, e1, postord, s2, e2):
        if s1 > e1 or s2 > e2:
            return None

        # root val will be from postord
        root_val = postord[e2]

        # find the root idx in inorder
        root_idx = find(inord, s1, e1, root_val)

        num_lst = root_idx - s1

        root = BinaryNode(root_val)
        # left subtree
        root.left = build(inord, s1, root_idx - 1, postord, s2, s2 + num_lst - 1)
        # right subtree
        root.right = build(inord, root_idx + 1, e1, postord, s2 + num_lst, e2 - 1)

        return root

    return build(A, 0, len(A) - 1, B, 0, len(B) - 1)


root = buildTree(
    [12, 4, 9, 15, 5, -1, 6, 19, 9, 10], [4, 15, 9, 12, -1, 19, 9, 10, 6, 5]
)

# create the tree
assert root.val == 5
# level 1
assert root.left.val == 12
assert root.right.val == 6

# level 2
assert root.left.right.val == 9
assert root.right.left.val == -1
assert root.right.right.val == 10

# level 3
assert root.right.right.left.val == 9
assert root.left.right.left.val == 4
assert root.left.right.right.val == 15

# level 4
assert root.right.right.left.left.val == 19
