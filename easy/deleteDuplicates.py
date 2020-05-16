# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: "ListNode") -> "ListNode":
        if head == None:
            return head
        n = head
        first_node = node = ListNode()
        while n != None:
            try:
                if n.val == n.next.val:
                    n = n.next
                else:
                    node.val = n.val
                    n = n.next
                    prev_node, node = node, ListNode()
                    prev_node.next = node
            except:
                node.val = n.val
                break
        return first_node

