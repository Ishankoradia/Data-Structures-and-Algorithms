"""
We know two ways of doing inorder traversal
1) recusion - TC: O(n) SC: O(H)
2) iterative - TC: O(n) SC: O(H)

The morris inorder traversal optimizes SC: O(1) keeping the TC same.
"""

from Trees.Implement.implementation import BinaryNode


def morris_inorder(root: BinaryNode):
    curr = root

    ans = []

    while curr is not None:
        if curr.left is None:
            ans.append(curr.val)
            curr = curr.right
        else:
            temp = curr.left
            while temp.right is not None and temp.right != curr:
                temp = temp.right

            if temp.right is None:
                temp.right = curr
                curr = curr.left

            if temp.right == curr:
                temp.right = None
                ans.append(curr.val)
                curr = curr.right

    return ans


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

assert morris_inorder(root) == [12, 4, 9, 15, 5, -1, 6, 19, 9, 10]
