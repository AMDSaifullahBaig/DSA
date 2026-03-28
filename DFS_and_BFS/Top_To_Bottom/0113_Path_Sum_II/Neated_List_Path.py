class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
    	self.result=[]
    	self.DFS(root,targetSum,[])
    	return self.result
    def DFS(self,root,targetSum,arr):
    	if not root:
    		return 
    	arr.append(root.val)
    	if root.val==targetSum and not root.left and not root.right:
    		self.result.append(list(arr))
    	else:
    		self.DFS(root.left,targetSum-root.val,arr)
    		self.DFS(root.right,targetSum-root.val,arr)
    	arr.pop()