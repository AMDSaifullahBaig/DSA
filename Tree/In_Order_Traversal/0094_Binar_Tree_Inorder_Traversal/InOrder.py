class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.result=[]
        self.DFS(root)
        return result
    def DFS(self,root):
    	if not root:
    	self.DFS(root.left)
    	self.result.append(root.val)
    	self.DFS(root.right)
    	return 