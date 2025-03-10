class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(self, list1, list2):
    dummy = node = ListNode()
    node1 = list1
    node2 = list2
    while node1 and node2:
        if node1.val <= node2.val:
            node.next = node1
            node1 = node1.next
        else:
            node.next = node2
            node2 = node2.next

        node = node.next

    node.next = node1 or node2

    return dummy.next