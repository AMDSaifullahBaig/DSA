class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def traverse(n):
            if not n:return 0
            l=traverse(n.left)
            r=traverse(n.right)
            return l+r
        return traverse(root)