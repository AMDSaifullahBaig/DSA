class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    	self.result=[]
    	self.DFS(root)
    	return self.result
    def DFS(self,root):
    	if not root:
    		return 
    	self.DFS(root.left)
    	self.DFS(root.right)
    	self.result.append(root.val)
    	return