class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
    	self.maximum=-float("inf")
    	self.DFS(root)
    	return self.maximum
    def DFS(self,root):
    	if not root:
    		return 0
    	l=max(0,self.DFS(root.left))
    	r=max(0,self.DFS(root.right))
    	add=l+r+root.val
    	self.maximum=max(self.maximum,add)
    	return root.val+max(l,r)