from implementation import BinaryNode

# data | left subtree | right subtree


def preorder_recursive(root: BinaryNode, ans=[]):
    if root is None:
        return
    ans.append(root.val)
    preorder_recursive(root.left, ans)
    preorder_recursive(root.right, ans)
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

assert [5, 12, 9, 4, 15, 6, -1, 10, 9, 19] == preorder_recursive(root, [])
