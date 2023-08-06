"""
Idea is inorder of a binary search tree is a sorted array in ascending order. 
So the kth smallest element is arr[k-1]. But we dont really need to keep an array, 
we can just maintain the count on the fly until we reach the kth smallest element.
"""

from Trees.Implement.implementation import BinaryNode
from Trees.BinarySearchTree.is_valid_bst import is_valid_bst
from Trees.Traversals.inorder import inorder_recursive


def traverse_kth_smallest_bst(root: BinaryNode, k: int, hm: dict = {}) -> None:
    if root is None:
        return

    traverse_kth_smallest_bst(root.left, k, hm)

    hm["count"] = hm.get("count", 0) + 1
    if hm["count"] == k:
        hm["ans"] = root.val

    traverse_kth_smallest_bst(root.right, k, hm)

    return hm


# test cases

# create the tree
root = BinaryNode(15)

# level 1
root.left = BinaryNode(10)
root.right = BinaryNode(21)

# level 2
root.left.left = BinaryNode(5)
root.right.right = BinaryNode(27)

# level 3
root.left.left.left = BinaryNode(1)
root.left.left.right = BinaryNode(8)
root.right.right.left = BinaryNode(24)
root.right.right.right = BinaryNode(34)

assert is_valid_bst(root) is True

for i, kth_smallest in enumerate(inorder_recursive(root, [])):
    assert traverse_kth_smallest_bst(root, i + 1, {})["ans"] == kth_smallest
