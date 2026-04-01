class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    	self.result=[]
    	self.DFS(root)
    	return self.result
    def DFS(self,root):
    	if not root:
    		return 
    	self.result.append(root.val)
    	self.DFS(root.left)
    	self.DFS(root.right)
    	return