"""
- You are given a linked list A
- Each node in the linked list contains two pointers: a next pointer and a random pointer
- The next pointer points to the next node in the list
- The random pointer can point to any node in the list, or it can be NULL
- Your task is to create a deep copy of the linked list A
- The copied list should be a completely separate linked list from the original list, but with the same node values and random pointer connections as the original list
- You should create a new linked list B, where each node in B has the same value as the corresponding node in A
- The next and random pointers of each node in B should point to the corresponding nodes in B (rather than A)
"""


class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


def copyRandomList(head):  # list to copy
    if head is None:
        return None

    curr = head
    # A->A'->B->B1->C->C'
    while curr is not None:
        nn = RandomListNode(curr.label)

        temp = curr.next
        curr.next = nn
        nn.next = temp

        curr = temp

    # random pointers
    curr = head
    while curr is not None:
        cloned_node = curr.next
        if curr.random:
            cloned_node.random = curr.random.next

        curr = cloned_node.next

    # separating out the cloned ll
    curr = head
    head2 = curr.next
    temp = curr.next

    while curr is not None:
        curr.next = curr.next.next

        if curr.next:
            temp.next = temp.next.next

            temp = temp.next

        curr = curr.next

    return head2
