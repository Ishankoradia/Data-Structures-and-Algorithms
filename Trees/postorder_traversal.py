from implementation import BinaryNode

# data | left subtree | right subtree


def postorder_recursive(root: BinaryNode, ans=[]):
    if root is None:
        return
    postorder_recursive(root.left, ans)
    postorder_recursive(root.right, ans)
    ans.append(root.val)
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

assert [4, 15, 9, 12, -1, 19, 9, 10, 6, 5] == postorder_recursive(root)
