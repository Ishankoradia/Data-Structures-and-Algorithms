"""
https://leetcode.com/problems/symmetric-tree/description/
"""

from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isPalindrome(self, arr) -> bool:
        i = 0
        j = len(arr) - 1
        while i <= j:
            if arr[i] != arr[j]:
                return False

            i += 1
            j -= 1

        return True

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        ###################################  iterative ###################################
        # q = deque()
        # q.append(root)

        # empty = -101

        # while len(q) > 0:
        #     sz = len(q)
        #     temp = []
        #     for i in range(sz):
        #         ele = q.popleft()
        #         temp.append(ele.val)

        #         if ele.val == empty: # leaf node
        #             continue

        #         if ele.left:
        #             q.append(ele.left)
        #         else:
        #             q.append(TreeNode(val=empty))

        #         if ele.right:
        #             q.append(ele.right)
        #         else:
        #             q.append(TreeNode(val=empty))

        #     if not self.isPalindrome(temp):
        #         return False

        # return True

        ###################################  recursive ###################################

        # just mirror any half (left or right) of the tree
        # this was a bit redundant
        # def mirrorHalf(root):
        #     if root is None:
        #         return

        #     temp = root.left
        #     root.left = root.right
        #     root.right = temp

        #     mirrorHalf(root.left)
        #     mirrorHalf(root.right)

        # # mirror all subtrees in left half
        # mirrorHalf(root.left)

        # instead of comparing left subtree with left subtree we compare opposite subtrees to
        # check whether they are mirrors or not
        def sameMirrorSubTree(p: Optional[TreeNode], q: Optional[TreeNode]):
            if not p and not q:
                return True

            if p and q and p.val == q.val:
                return sameMirrorSubTree(p.left, q.right) and sameMirrorSubTree(
                    p.right, q.left
                )

            return False

        return sameMirrorSubTree(root.left, root.right)
