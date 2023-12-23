"""
You are given an integer array A denoting the Level Order Traversal of the Binary Tree.

You have to Deserialize the given Traversal in the Binary Tree and return the root of the Binary Tree.

NOTE:

In the array, the NULL/None child is denoted by -1.
For more clarification check the Example Input.
"""
from Trees.Implement.implementation import BinaryNode
from collections import deque


def deserialize(A: BinaryNode):
    root = BinaryNode(A[0])

    q = deque()

    q.append(root)

    c = 0
    while len(q) > 0:
        sz = len(q)

        for _ in range(sz):
            nn: BinaryNode = q.popleft()

            c += 1
            if c < len(A) and A[c] != -1:
                nn.left = BinaryNode(A[c])
                q.append(nn.left)

            c += 1
            if c < len(A) and A[c] != -1:
                nn.right = BinaryNode(A[c])
                q.append(nn.right)

    return root
