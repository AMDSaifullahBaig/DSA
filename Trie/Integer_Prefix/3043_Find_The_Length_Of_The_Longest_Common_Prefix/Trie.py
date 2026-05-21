class Node():
    def __init__(self):
    		self.child=[None]*10
class trie():
    	def __init__(self):
    		self.root=Node()
    	def insert(self,nums):
    		node=self.root
    		for i in str(nums):
    			idx=int(i)
    			if not node.child[idx]:
    				node.child[idx]=Node()
    			node=node.child[idx]
    	def prefix(self,nums):
    			node=self.root
    			length=0
    			for i in str(nums):
    				idx=int(i)
    				if node.child[idx]:
    					length+=1
    					node=node.child[idx]
    				else:
    					break
    			return length
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        node=trie()
        for i in arr1:
        	node.insert(i)
        maximum=0
        for i in arr2:
        	l=node.prefix(i)
        	maximum=max(maximum,l)
        return maximum