from Trees.Implement.implementation import BinaryNode
from Trees.BinarySearchTree.is_valid_bst import is_valid_bst
from Trees.BinarySearchTree.search import search_bst


# create bst from sorted array
def create_bst(arr: list, start: int, end: int):
    if start > end:
        return None
    mid = (start + end) // 2
    root = BinaryNode(arr[mid])

    root.left = create_bst(arr, start, mid - 1)
    root.right = create_bst(arr, mid + 1, end)

    return root


root = create_bst([5, 10, 15, 20, 25, 30], 0, 5)
assert is_valid_bst(root) is True
assert search_bst(root, 5) is True
assert search_bst(root, 10) is True
assert search_bst(root, 15) is True
assert search_bst(root, 20) is True
assert search_bst(root, 25) is True
assert search_bst(root, 30) is True
assert search_bst(root, 35) is False
