from implementation import BinaryNode

# left subtree | data | right subtree


def inorder_recursive(root: BinaryNode, ans=[]):
    if root is None:
        return
    inorder_recursive(root.left, ans)
    ans.append(root.val)
    inorder_recursive(root.right, ans)
    return ans


# create the tree
root = BinaryNode(5)
# level 1
root.left = BinaryNode(12)
root.right = BinaryNode(6)

# level 2
root.left.right = BinaryNode(9)
root.right.left = BinaryNode(-1)
root.right.right = BinaryNode(10)

# level 3
root.right.right.left = BinaryNode(9)
root.left.right.left = BinaryNode(4)
root.left.right.right = BinaryNode(15)

# level 4
root.right.right.left.left = BinaryNode(19)

assert inorder_recursive(root) == [12, 4, 9, 15, 5, -1, 6, 19, 9, 10]
