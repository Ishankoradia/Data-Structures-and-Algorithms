from Trees.Implement.implementation import BinaryNode


first = None
second = None
prev = None


def recover_bst_recursive(root: BinaryNode):
    """Function"""
    global first
    global second
    global prev

    if root is None:
        return

    recover_bst_recursive(root.left)

    if prev is not None and prev.val > root.val:
        if first is None:
            first = prev
            second = root
        else:
            second = root

    prev = root

    recover_bst_recursive(root.right)

    return (first, second, prev)


def recover_bst_iterative(root: BinaryNode):
    """Function bst traversal"""

    curr = root

    f = None
    s = None
    p = None

    while curr is not None:
        if curr.left is None:
            if p is not None and p.val > curr.val:
                if f is None:
                    f = p
                    s = curr
                else:
                    s = curr

            p = curr
            curr = curr.right
        else:
            temp = curr.left
            while temp.right is not None and temp.right != curr:
                temp = temp.right

            if temp.right is None:
                temp.right = curr
                curr = curr.left

            if temp.right == curr:
                temp.right = None
                if p is not None and p.val > curr.val:
                    if f is None:
                        f = p
                        s = curr
                    else:
                        s = curr
                p = curr
                curr = curr.right
    # self.recover(A)

    return [s.val, f.val]


root = BinaryNode(2)
root.left = BinaryNode(3)
root.right = BinaryNode(1)

recover_bst_recursive(root)

assert [first.val, second.val] == [3, 1]


assert recover_bst_iterative(root) == [1, 3]
