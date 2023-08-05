"""
Vertical order is fetching nodes that are at the same vertical level. 
There are two ways we could go
1) DFS (recursion) : In this we will be able to find all nodes at a vertical level but they will not be in the correct order
2) BFS (breadth first search) : We will be able tofind all nodes at a vertical level with the correct order of top to bottom.
We will assuming root is at level 0 and going left the level would be -1,-2,-3.... and going right the level would be 1,2,3....
"""
from collections import deque
from Trees.Implement.implementation import BinaryNode, Pair


def verticalorder(root: BinaryNode) -> list[list[int]]:
    q = deque()
    pair = Pair(root, 0)
    q.append(pair)
    # to store node vals for each level
    max_level = 0
    min_level = 0
    hm = dict()
    ans = []

    while len(q) > 0:
        top: Pair = q.popleft()
        if top.state in hm:
            hm.get(top.state, 0).append(top.node.val)
        else:
            hm[top.state] = [top.node.val]

        max_level = max(max_level, top.state)
        min_level = min(min_level, top.state)

        if top.node.left is not None:
            left_pair: Pair = Pair(top.node.left, top.state - 1)
            q.append(left_pair)

        if top.node.right is not None:
            right_pair: Pair = Pair(top.node.right, top.state + 1)
            q.append(right_pair)

    for level in range(min_level, max_level + 1):
        ans.append(hm[level])

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


vertical_levels = verticalorder(root)

assert vertical_levels[0] == [6]
assert vertical_levels[1] == [5, 14]
assert vertical_levels[2] == [2, 9, 15]
assert vertical_levels[3] == [1, 8, 10, 12, 16]
assert vertical_levels[4] == [3, 7, 4]
assert vertical_levels[5] == [13, 11]
