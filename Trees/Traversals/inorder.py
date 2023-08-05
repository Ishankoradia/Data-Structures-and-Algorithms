from implementation import BinaryNode, Pair

# left subtree | data | right subtree


############ recursive ############
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


############ iterative ############
# states
# 1) call left child
# 2) print/append data
# 3) call right child


def inorder_iterative(root: BinaryNode):
    ans = []
    # initialize a stack
    st = list()
    p = Pair(root, 1)
    st.append(p)
    while len(st) > 0:
        top: Pair = st[-1]
        if top.state == 1:
            top.state += 1
            if top.node.left is not None:
                st.append(Pair(top.node.left, 1))

        elif top.state == 2:
            ans.append(top.node.val)
            top.state += 1
            if top.node.right is not None:
                st.append(Pair(top.node.right, 1))

        elif top.state == 3:
            st.pop()

    return ans


assert inorder_iterative(root) == [12, 4, 9, 15, 5, -1, 6, 19, 9, 10]
