class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
    	return self.DFS(root,float('inf'),float('inf')
    def DFS(self,root,l,u):
    	if not root:return True
    	if not(l<root.val<u):
    		return False
    	return self.DFS(root.left,l,root.val) and self.DFS(root.right,root.val,u)