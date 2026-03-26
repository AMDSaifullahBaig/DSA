class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
        	return 0
        l=self.maxDepth(root.left)
        r=self.maxDepth(root.right)
        return 1+max(l,r)