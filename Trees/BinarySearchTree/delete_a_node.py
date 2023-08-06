from Trees.Implement.implementation import BinaryNode
from Trees.BinarySearchTree.max_bst import max_bst
from Trees.BinarySearchTree.is_valid_bst import is_valid_bst
from Trees.BinarySearchTree.search import search_bst

# from Trees.BinarySearchTree.min_bst import min_bst


def delete_node_bst(root: BinaryNode, k: int):
    if k < root.val:
        root.left = delete_node_bst(root.left, k)
    elif k > root.val:
        root.right = delete_node_bst(root.right, k)
    else:
        if root.left is None and root.right is None:  # the node has 0 child
            return None
        elif (
            root.left is None and root.right is not None
        ):  # the node has 1 child on the right
            return root.right
        elif (
            root.left is not None and root.right is None
        ):  # the node has 1 child on the left
            return root.left
        else:  # the node has 2 children on left and right
            # anyone of the below can be used
            # either we replace the curr node with max from lst
            # or we replace the curr node wth min from rst
            val = max_bst(root.left)
            # val = min_bst(root.right)

            root.val = val
            root.left = delete_node_bst(root.left, val)
            # root.right = delete_node_bst(root.right, val)

    return root


# test cases

# create the tree
root = BinaryNode(35)

# level 1
root.left = BinaryNode(20)
root.right = BinaryNode(41)

# level 2
root.left.left = BinaryNode(10)
root.left.right = BinaryNode(30)
root.right.right = BinaryNode(51)

# level 3
root.left.left.left = BinaryNode(5)
root.right.right.left = BinaryNode(47)
root.right.right.right = BinaryNode(60)

# level 4
root.right.right.left.left = BinaryNode(45)
root.right.right.left.right = BinaryNode(48)
root.right.right.right.left = BinaryNode(55)
root.right.right.right.right = BinaryNode(70)

# level 5
root.right.right.left.left.right = BinaryNode(46)
root.right.right.right.right.right = BinaryNode(75)


assert is_valid_bst(root) is True

# delete a node
assert search_bst(root, 5) is True
delete_node_bst(root, 5)
assert search_bst(root, 5) is False
assert is_valid_bst(root) is True

# delete a node
assert search_bst(root, 41) is True
delete_node_bst(root, 41)
assert search_bst(root, 41) is False
assert is_valid_bst(root) is True

# delete a node

assert search_bst(root, 51) is True
delete_node_bst(root, 51)
assert search_bst(root, 51) is False
assert is_valid_bst(root) is True
