class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
    	return self.recursion(root)!=-1
    def recursion(self,root):
    	if not root:return 0
    	l=self.recursion(root.left)
    	if l==-1:return -1
    	r=self.recursion(root.right)
    	if  r==-1:return -1
    	if abs(l-r)>1:return -1
    	return 1+max(l,r)