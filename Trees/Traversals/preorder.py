from Trees.Implement.implementation import BinaryNode, Pair

# data | left subtree | right subtree


############ recursive ############
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


############ iterative ############
# states
# 1) data
# 2) call left child
# 3) call right child


def preorder_iterative(root: BinaryNode):
    ans = []
    # initialize a stack
    st = list()
    p = Pair(root, 1)
    st.append(p)
    while len(st) > 0:
        top: Pair = st[-1]
        if top.state == 1:
            ans.append(top.node.val)
            top.state += 1
            if top.node.left is not None:
                st.append(Pair(top.node.left, 1))

        elif top.state == 2:
            top.state += 1
            if top.node.right is not None:
                st.append(Pair(top.node.right, 1))

        elif top.state == 3:
            st.pop()

    return ans


assert preorder_iterative(root) == [5, 12, 9, 4, 15, 6, -1, 10, 9, 19]
