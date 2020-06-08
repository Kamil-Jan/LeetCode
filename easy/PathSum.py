from collections import deque


def is_leaf(node):
    return node.left == node.right

class Solution:
    def hasPathSum(self, root, sum: int) -> bool:
        if not root:
            return
        stack = deque([(root, sum)])
        while stack:
            root, remain_sum = stack.pop()
            if root:
                if is_leaf(root):
                    if root.val == remain_sum:
                        return True
                else:
                    stack.append((root.right, remain_sum - root.val))
                    stack.append((root.left, remain_sum - root.val))
        return False

