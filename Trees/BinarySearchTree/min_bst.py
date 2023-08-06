from Trees.Implement.implementation import BinaryNode


def min_bst(root: BinaryNode):
    curr = root

    while curr.left is not None:
        curr = curr.left

    return curr.val
