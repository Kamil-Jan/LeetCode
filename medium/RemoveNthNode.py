from collections import deque


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        stack = deque()
        node = head
        while node:
            stack.append(node)
            node = node.next

        if n + 1 <= len(stack):
            prev_del_node = stack[-n - 1]
            prev_del_node.next = prev_del_node.next.next
            return head
        return stack[-n].next
