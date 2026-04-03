class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    	if not root or root.val==val:
    		return root
    	if root.val>val:
    		self.searchBST(root.left,val)
    	self.searchBST(root.right,val)