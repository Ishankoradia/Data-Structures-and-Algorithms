"""
LCA : lowest common ancestor of two nodes
Find root to node path for both the nodes and find out the highest common element
"""
import sys

sys.setrecursionlimit(10**9)
from Trees.Implement.implementation import BinaryNode
from Trees.node_to_root_path import node_to_root_path


def lca_bt(root: BinaryNode, k1: int, k2: int):
    """TC: O(n) but SC: O(n)"""
    arr1 = node_to_root_path(root, k1)
    arr2 = node_to_root_path(root, k2)

    ans = None
    for i in range(min(len(arr1), len(arr2))):
        i_end = len(arr1) - 1 - i
        j_end = len(arr2) - 1 - i
        if arr1[i_end] == arr2[j_end]:
            ans = arr1[i_end]
        else:
            break

    return ans


def lca_bt_v1(root: BinaryNode, k1: int, k2: int):
    """TC: O(n) but SC: O(1)"""

    def find(root, x):
        if root is None:
            return False

        l = find(root.left, x)
        r = find(root.right, x)

        if l or r or root.val == x:
            return True

        return False

    if find(root, k1) is False or find(root, k2) is False:
        return -1

    def find_lca(root, k1, k2):
        if root is None:
            return None

        l = find_lca(root.left, k1, k2)
        r = find_lca(root.right, k1, k2)

        if root.val in [k1, k2]:
            return root.val
        else:
            if l is None and r is None:
                return None
            elif l is None and r is not None:
                return r
            elif l is not None and r is None:
                return l
            else:
                return root.val

    return find_lca(root, k1, k2)


# test cases

# create tree

# level 1
root = BinaryNode(1)

# level 2
root.left = BinaryNode(2)
root.right = BinaryNode(3)

# level 3
root.left.left = BinaryNode(4)
root.right.left = BinaryNode(5)
root.right.right = BinaryNode(6)

# level 4
root.right.left.left = BinaryNode(7)
root.right.right.left = BinaryNode(8)
root.right.right.right = BinaryNode(9)

assert lca_bt(root, 4, 6) == 1
assert lca_bt(root, 5, 6) == 3
assert lca_bt(root, 7, 8) == 3
assert lca_bt(root, 6, 9) == 6

assert lca_bt_v1(root, 4, 6) == 1
assert lca_bt_v1(root, 5, 6) == 3
assert lca_bt_v1(root, 7, 8) == 3
assert lca_bt_v1(root, 6, 9) == 6
assert lca_bt_v1(root, 10, 9) == -1
