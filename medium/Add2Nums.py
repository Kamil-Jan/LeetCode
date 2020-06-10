# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = l1
        while l1:
            l1.val += l2.val

            if l1.val > 9:
                if l1.next:
                    l1.next.val += 1
                else:
                    l1.next = ListNode(1)
                l1.val = l1.val % 10

            if not l1.next:
                l1.next = l2.next
                break
            l1 = l1.next

            if l2.next:
                l2 = l2.next
            else:
                l2 = ListNode(0)

        return root

