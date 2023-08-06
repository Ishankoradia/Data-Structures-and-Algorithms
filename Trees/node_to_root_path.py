from Trees.Implement.implementation import BinaryNode


def node_to_root_path(root: BinaryNode, k: int):
    ans = []

    def search_bt(root: BinaryNode, k: int, ans: list = []):
        if root is None:
            return False

        if root.val == k:
            ans.append(root.val)
            return True

        if search_bt(root.left, k, ans) is True:
            ans.append(root.val)
            return True

        if search_bt(root.right, k, ans) is True:
            ans.append(root.val)
            return True

        return False

    search_bt(root, k, ans)

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

ans = []
assert node_to_root_path(root, 15) == [15, 9, 12, 5]
assert node_to_root_path(root, -1) == [-1, 6, 5]
assert node_to_root_path(root, 19) == [19, 9, 10, 6, 5]
