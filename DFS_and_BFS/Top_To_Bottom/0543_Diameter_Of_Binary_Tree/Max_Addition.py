class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    	self.dia=0
    	self.DFS(root)
    	return self.dia
    def DFS(self,root):
    	if not root:return 0
    	l=self.DFS(root.left)
    	r=self.DFS(root.right)
    	self.dia=max(l+r,self.dia)
    	return 1+max(l,r)