# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head:
            h = head.next
            if head.next:
                h.next, head.next = head, h.next
                head.next = self.swapPairs(head.next)
                return h
        return head

    def swapPairsIterative(self, head: ListNode) -> ListNode:
        if not head:
            return
        node = head
        while node.next:
            node.val, node.next.val = node.next.val, node.val
            if node.next.next:
                node = node.next.next
            else:
                break
        return head
