"""
Given a binary tree, return the zigzag level order traversal of its nodes values. 
(ie, from left to right, then right to left for the next level and alternate between).
"""
from collections import deque
from Trees.Implement.implementation import BinaryNode


def zigzag_level_order(A: BinaryNode):
    q = deque()

    q.append(A)

    ans = []
    flag = 0

    while len(q) > 0:
        sz = len(q)

        temp = [0] * sz

        for i in range(sz):
            nn: BinaryNode = q.popleft()

            if nn.left:
                q.append(nn.left)

            if nn.right:
                q.append(nn.right)

            if flag:
                temp[sz - i - 1] = nn.val
            else:
                temp[i] = nn.val

        ans.append(temp)

        flag = 1 - flag

    return ans
