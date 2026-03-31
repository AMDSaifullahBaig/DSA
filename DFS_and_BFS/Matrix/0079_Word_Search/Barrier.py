class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
    	self.m=len(board)
    	self.n=len(board[0])
    	for i in range(self.m):
    		for j in range(self.n):
    			if self.dfs(board,i,j,word,0):
    				return True
    	return False
    def dfs(self,board,r,c,word,e):
        if c>=self.n or c<0 or r>=self.m or r<0:return False
        if board[r][c]!=word[e]:
        	return False
        if e==len(word)-1:
        	return True
        temp=board[r][c]
        board[r][c]="#"
        
        found=(self.dfs(board,r,c-1,word,e+1) or\
        self.dfs(board,r,c+1,word,e+1) or\ 
        self.dfs(board,r+1,c,word,e+1) or\
        self.dfs(board,r-1,c, word,e+1))
        
        board[r][c]=temp
        return found