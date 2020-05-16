class Solution:
    def mergeTwoLists(self, l1, l2):
        i = l1
        j = l2
        if i == None and j == None:
            return i
        first_node = node = ListNode()

        while i != None and j != None:
            if i.val <= j.val:
                node.val = i.val
                i = i.next
            else:
                node.val = j.val
                j = j.next
            prev_node, node = node, ListNode()
            prev_node.next = node

        while i != None:
            node.val = i.val
            if i.next != None:
                prev_node, node = node, ListNode()
                prev_node.next = node
            i = i.next

        while j != None:
            node.val = j.val
            if j.next != None:
                prev_node, node = node, ListNode()
                prev_node.next = node
            j = j.next
        return first_node

