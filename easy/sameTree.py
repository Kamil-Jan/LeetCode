# Definition for a binary tree node.
class Solution:
    def isSameTree(self, p: "TreeNode", q: "TreeNode") -> bool:
        def check(node1, node2):
            if node1 == node2:
                return True
            if node1 == None or node2 == None:
                return False
            if node1.val == node2.val:
                return check(node1.left, node2.left) and check(node1.right, node2.right)

        return check(p, q)

