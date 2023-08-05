"""
Right view of trees contains all the nodes that can be seen at each level from the right side.
Since we know how to print nodes at a level, printing the last node at each level can give us the right view.
"""

from collections import deque
from Trees.Implement.implementation import BinaryNode


def right_tree_view(root: BinaryNode) -> list[int]:
    q = deque()
    q.append(root)
    ans = []

    while len(q) > 0:
        size = len(q)
        for i in range(size):
            ele: BinaryNode = q.popleft()
            if i == (size - 1):
                ans.append(ele.val)

            # append the left of the curr node
            if ele.left is not None:
                q.append(ele.left)

            # append the right of the curr node
            if ele.right is not None:
                q.append(ele.right)

    return ans


# test cases

# create the tree
root = BinaryNode(1)
# level 1
root.left = BinaryNode(2)
root.right = BinaryNode(3)

# level 2
root.left.left = BinaryNode(4)
root.left.right = BinaryNode(11)
root.right.right = BinaryNode(19)

# level 3
root.left.left.left = BinaryNode(7)
root.left.right.right = BinaryNode(25)
root.right.right.left = BinaryNode(-3)
root.right.right.right = BinaryNode(45)

assert right_tree_view(root) == [1, 3, 19, 45]
