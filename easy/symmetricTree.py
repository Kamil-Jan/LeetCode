class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isSymSubTree(node1, node2):
            if node1 == None or node2 == None:
                return node1 == node2
            if node1.val != node2.val:
                return False
            return isSymSubTree(node1.left, node2.right) and isSymSubTree(node1.right, node2.left)

        if not root:
            return True
        return isSymSubTree(root, root)
