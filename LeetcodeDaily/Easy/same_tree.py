from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderTraversal(self, root: Optional[TreeNode]):
        q = deque()
        q.append(root)

        if root is None:
            return []

        ans = []
        while len(q) > 0:
            ele = q.popleft()
            ans.append(ele.val)

            if ele.val is None:  # leaf node
                continue

            if ele.left is not None:
                q.append(ele.left)
            else:
                q.append(TreeNode(val=None))

            if ele.right is not None:
                q.append(ele.right)
            else:
                q.append(TreeNode(val=None))

        return ans

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # #solution using level order
        # return self.levelOrderTraversal(p) == self.levelOrderTraversal(q)

        if not p and not q:
            return True

        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        return False
