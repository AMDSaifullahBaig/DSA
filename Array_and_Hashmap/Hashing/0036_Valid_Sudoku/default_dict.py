class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=defaultdict(set)
        column=defaultdict(set)
        box=defaultdict(set)
        for i in range(9):
        	for j in range(9):
        		e=board[i][j]
        		if e==".":continue
        		if e in row[i] or e in column[j] or e in box[(i//3,j//3)]:
        			return False
        		row[i].add(e)
        		column[j].add(e)
        		box[(i//3,j//3)].add(e)
        return True