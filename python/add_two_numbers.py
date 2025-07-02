'''
You are given two non-empty linked lists, l1 and l2, where each represents a non-negative integer.

The digits are stored in reverse order, e.g. the number 123 is represented as 3 -> 2 -> 1 -> in the linked list.

Each of the nodes contains a single digit. You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Return the sum of the two numbers as a linked list.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def add_two_numbers(self, l1, l2):
        if not l1 or not l2:
            return []

        def get_num(l):
            i = 0
            res = 0
            while l:
                res += l.val * (10 ** i)
                i += 1
                l = l.next
            return res
        
        num1 = get_num(l1)
        num2 = get_num(l2)
        res = num1 + num2

        new = head = ListNode()
        while res != 0:
            newNode = ListNode()
            new.val = res % 10
            res = res // 10
            if res != 0:
                new.next = newNode
                new = new.next

        return head