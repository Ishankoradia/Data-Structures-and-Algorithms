"""
LCA : lowest common ancestor of two nodes
Find root to node path for both the nodes and find out the highest common element
"""
from Trees.Implement.implementation import BinaryNode
from Trees.node_to_root_path import node_to_root_path


def lca_bt(root: BinaryNode, k1: int, k2: int):
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
