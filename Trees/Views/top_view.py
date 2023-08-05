"""
Left view of trees contains all the nodes that can be seen at each vertical level from the top side.
Since we know how to print nodes at a each vertical level, printing the first node at each level can give us the top view.
"""

from Trees.Implement.implementation import BinaryNode
from Trees.Traversals.verticalorder import verticalorder


def top_tree_view(root: BinaryNode):
    vert_order = verticalorder(root)

    ans = []
    for level in vert_order:
        ans.append(level[0])

    return ans


# test cases

# create the tree
root = BinaryNode(1)
# level 1
root.left = BinaryNode(2)
root.right = BinaryNode(3)

# level 2
root.left.left = BinaryNode(5)
root.left.right = BinaryNode(8)
root.right.left = BinaryNode(10)
root.right.right = BinaryNode(13)

# level 3
root.left.left.left = BinaryNode(6)
root.right.left.left = BinaryNode(9)
root.right.left.right = BinaryNode(7)
root.right.right.left = BinaryNode(4)

# level 4
root.left.left.left.right = BinaryNode(14)
root.right.right.left.left = BinaryNode(12)
root.right.right.left.right = BinaryNode(11)

# level 5
root.left.left.left.right.right = BinaryNode(15)

# level 6
root.left.left.left.right.right.right = BinaryNode(16)


assert top_tree_view(root) == [6, 5, 2, 1, 3, 13]
