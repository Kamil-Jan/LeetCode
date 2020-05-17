class Solution:
    def levelOrderBottom(self, root):
        def bottomUp(node, level):
            if not node:
                return
            try:
                orderTraversal[level].append(node.val)
            except:
                orderTraversal.insert(0, [node.val])
            bottomUp(node.left, level - 1)
            bottomUp(node.right, level - 1)

        if not root:
            return []
        orderTraversal = []
        bottomUp(root.left, -1)
        bottomUp(root.right, -1)
        orderTraversal.append([root.val])

        return orderTraversal

