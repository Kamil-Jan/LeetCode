# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepthRecursive(self, root: TreeNode) -> int:
        def countDepth(node):
            if not node:
                return 0
            return 1 + max(countDepth(node.left), countDepth(node.right))

        if not root:
            return 0
        return 1 + max(countDepth(root.left), countDepth(root.right))

    def maxDepthIterative(self, root):
        if not root:
            return 0
        stack = [(root, 1)]
        maximumDepth = 1
        while stack:
            temp = stack.pop()
            if temp[0]:
                # node is not None
                maximumDepth = max(temp[1], maximumDepth)
                stack.extend([(temp[0].right, temp[1] + 1), (temp[0].left, temp[1] + 1)])
        return maximumDepth

