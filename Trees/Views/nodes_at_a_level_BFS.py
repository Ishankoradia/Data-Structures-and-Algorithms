from collections import deque
from Trees.Implement.implementation import BinaryNode


def nodes_at_level(root: BinaryNode) -> list[list[int]]:
    q = deque()
    q.append(root)
    ans = []

    while len(q) > 0:
        size = len(q)
        level_arr = []
        for _ in range(size):
            ele: BinaryNode = q.popleft()
            level_arr.append(ele.val)

            # append the left of the curr node
            if ele.left is not None:
                q.append(ele.left)

            # append the right of the curr node
            if ele.right is not None:
                q.append(ele.right)

        ans.append(level_arr)

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

levels = nodes_at_level(root)

assert levels[0] == [1]
assert levels[1] == [2, 3]
assert levels[2] == [4, 11, 19]
assert levels[3] == [7, 25, -3, 45]
