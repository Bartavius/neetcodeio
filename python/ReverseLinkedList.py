class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
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