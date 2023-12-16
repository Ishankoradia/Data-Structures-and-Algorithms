from Trees.Implement.implementation import BinaryNode, Pair

# left subtree | right subtree | data


############ recursive ############
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


############ iterative ############
# states
# 1) call left child
# 2) call right child
# 3) print/append data


def postorder_iterative(root: BinaryNode):
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
            top.state += 1
            if top.node.right is not None:
                st.append(Pair(top.node.right, 1))

        elif top.state == 3:
            ans.append(top.node.val)
            st.pop()

    return ans


assert postorder_iterative(root) == [4, 15, 9, 12, -1, 19, 9, 10, 6, 5]
