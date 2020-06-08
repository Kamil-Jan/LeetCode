class Solution:
    def hasCycle(self, head) -> bool:
        while head:
            head.visited = True
            try:
                if head.next.visited:
                    return True
            except:
                head = head.next
        return False

