class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        lh = self.minDepth(root.left)
        rh = self.minDepth(root.right)
        if lh and rh:
            return 1 + min(lh, rh)
        elif lh:
            return lh + 1
        elif rh:
            return rh + 1
        else:
            return 1
