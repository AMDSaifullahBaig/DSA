class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
    	self.hash=defaultdict(list)
    	self.DFS(root,0,0)
    	results=[]
    	for col in sorted(self.hash.keys()):
    		e=sorted(self.hash[col])
    		results.append([value for row,value in e])
    	return results
    def DFS(self,root,row,column):
    	if not root:
    		return 
    	self.hash[column].append([row,root.val])
    	self.DFS(root.left,row+1,column-1)
    	self.DFS(root.right,row+1,column+1)