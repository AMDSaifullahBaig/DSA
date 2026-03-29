class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
    	self.add=0
    	self.DFS(root)
    	return self.add
    def DFS(self,root):
        if not root:
            return 0
        l=self.DFS(root.left)
        r=self.DFS(root.right)
        if root.left and l==1:
        	self.add+=root.left.val
        return max(l,r)+1