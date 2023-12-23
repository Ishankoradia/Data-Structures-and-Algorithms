"""
Given a binary search tree A, where each node contains a positive integer, and an integer B, 
you have to find whether or not there exist two different nodes X and Y such that X.value + Y.value = B.

Return 1 to denote that two such nodes exist. Return 0, otherwise
"""
from Trees.Implement.implementation import BinaryNode


def t2Sum(A: BinaryNode, B):
    """SC: O(N) - to store the extra inorder array"""

    def traverse(root: BinaryNode, ans=[]):
        if root is None:
            return None

        traverse(root.left)
        ans.append(root.val)
        traverse(root.right)

        return ans

    inorder = traverse(A)  # sorted

    p1 = 0
    p2 = len(inorder) - 1

    while p1 < p2:
        if inorder[p1] + inorder[p2] > B:
            p2 -= 1
        elif inorder[p1] + inorder[p2] < B:
            p1 += 1
        else:
            return 1

    return 0


# Can we do it in space of O(H) ???
def t2Sum_optimized(A: BinaryNode, B):
    st1 = []  # stack of nodes for forward bst iterator - iterate in increasing order
    st2 = []  # stack of nodes for backward bst iterator - iterate in decreasing order

    curr: BinaryNode = A
    while curr is not None:
        st1.append(curr)
        curr = curr.left

    curr: BinaryNode = A
    while curr is not None:
        st2.append(curr)
        curr = curr.right

    while len(st1) > 0 and len(st2) > 0:
        if st1[-1] == st2[-1]:  # pointers are pointing to the same node
            return 0

        if st1[-1].val + st2[-1].val > B:
            nn: BinaryNode = st2.pop()
            curr = nn.left
            while curr is not None:
                st2.append(curr)
                curr = curr.right

        elif st1[-1].val + st2[-1].val < B:
            nn: BinaryNode = st1.pop()
            curr = nn.right
            while curr is not None:
                st1.append(curr)
                curr = curr.left
        else:
            return 1

    return 0
