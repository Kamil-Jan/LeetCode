class Solution:
    def isBalanced(self, root) -> bool:
        def count_height(node):
            if not node:
                return 0
            left = count_height(node.left)
            right = count_height(node.right)
            if bf != []:
                return
            elif abs(left - right) > 1:
                bf.append(left - right)
                return
            return 1 + max(left, right)

        if not root:
            return True
        bf = []
        count_height(root)
        return bf == []

