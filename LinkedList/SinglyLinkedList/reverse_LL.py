from implement import ListNode


def reverse_list(head):
    prev = None
    curr = head

    while curr != None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev


# testing
# create node list [1,2,3,4,5]
curr = None
head = None
input = ""
for val in [1, 2, 3, 4, 5]:
    input += f"{val} "
    if curr is None:
        head = ListNode(val)
        curr = head
    else:
        curr.next = ListNode(val)
        curr = curr.next

reverse_head = reverse_list(head)

# print the output
ans = ""
while reverse_head != None:
    ans += f"{reverse_head.data} "
    reverse_head = reverse_head.next

print("input", input)
print("output", ans)
