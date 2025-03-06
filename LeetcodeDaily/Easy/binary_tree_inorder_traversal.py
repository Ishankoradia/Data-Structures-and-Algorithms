"""
https://leetcode.com/problems/binary-tree-inorder-traversal/description/
"""

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # inorder means : left, current, right
        # recursion
        global ans
        ans = []

        def dfs(node: Optional[TreeNode]):
            if node == None:
                return
            dfs(node.left)
            ans.append(node.val)
            dfs(node.right)

        dfs(root)

        return ans
