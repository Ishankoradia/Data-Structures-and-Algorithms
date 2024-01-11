"""
Given the root of a binary tree, 
find the maximum value v for which there exist different nodes a and b 
where v = |a.val - b.val| and a is an ancestor of b.

A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.
"""
from Trees.Implement.implementation import BinaryNode


def max_ancestor_diff_brute(root: BinaryNode) -> int:
    """Brute force approach with SC:O(H) TC:O(N*2)"""
    global st
    global ans
    ans = 0
    st = []

    def dfs(root):
        global st
        global ans
        if root is None:
            return

        st.append(root.val)

        dfs(root.left)

        for x in st:
            ans = max(ans, abs(x - root.val))

        dfs(root.right)

        st.pop()

    dfs(root)

    return ans


def max_ancestor_diff_brute(root: BinaryNode) -> int:
    """Instead of comparing each node with each other node we just keep a track max & min from node to root"""
    global ans
    ans = 0

    def dfs(root: BinaryNode, curr_max, curr_min):
        global ans
        if root is None:
            return

        ans = max(ans, abs(root.val - curr_max), abs(root.val - curr_min))
        curr_max = max(curr_max, root.val)
        curr_min = min(curr_min, root.val)

        dfs(root.left, curr_max, curr_min)
        dfs(root.right, curr_max, curr_min)

    dfs(root, root.val, root.val)

    return ans
