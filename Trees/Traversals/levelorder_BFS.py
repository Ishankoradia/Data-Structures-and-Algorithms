"""
 Breadth first search or also called level order traversal. 
 This method traverses the tree breadth wise.
"""
from collections import deque
from Trees.Implement.implementation import BinaryNode


def levelorder(root: BinaryNode):
    q = deque()
    q.append(root)
    ans = []
    while len(q) > 0:
        ele: BinaryNode = q.popleft()
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


assert levelorder(root) == [1, 2, 3, 4, 11, 19, 7, 25, -3, 45]
