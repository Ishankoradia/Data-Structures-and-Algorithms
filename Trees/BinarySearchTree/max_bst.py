from Trees.Implement.implementation import BinaryNode


def max_bst(root: BinaryNode):
    curr = root

    while curr.right is not None:
        curr = curr.right

    return curr.val
