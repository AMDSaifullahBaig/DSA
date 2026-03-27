class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.dfs(root.left,root.right)
    def dfs(self,left,right):
        if not left and not right:
            return True
        if not left or not right or left.val!=right.val:
            return False  
        return self.dfs(left.left,right.right) and self.dfs(left.right,right.left)