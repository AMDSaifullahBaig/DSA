class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    	self.result=[]
    	self.DFS(root,0)
    	return self.result
    def DFS(self,root,depth):
    	if not root:return 
    	if depth==len(self.result):
    		self.result.append(root.val)
    	self.DFS(root.right)
    	self.DFS(root.left)