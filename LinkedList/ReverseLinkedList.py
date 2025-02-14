def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return head

    tail = head.next
    node = head
    node.next = None

    while tail:
        temp = tail
        tail = tail.next
        temp.next = node
        node = temp

    return node