class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
    	m=len(grid)
    	n=len(grid[0])
    	minimum=min(m//2,n//2)
    	for i in range(minimum):
    		row=[]
    		col=[]
    		val=[]
    		for l in range(i,m-i-1):
    			row.append(l)
    			col.append(i)
    			val.append(grid[l][i])
    		for b in range(i,n-i-1):
    			row.append(m-i-1)
    			col.append(b)
    			val.append(grid[m-i-1][b])
    		for r in range(m-i-1,i,-1):
    			row.append(r)
    			col. append(n-i-1)
    			val.append(grid[r][n-i-1])
    		for t in range(n-i-1,i,-1):
    			row. append(i)
    			col.append(t)
    			val.append(grid[i][t])
    		total=len(val)
    		reduced=k%total
    		for i in range(total):
    			idx=(i-reduced+total)%total
    			grid[row[i]][col[i]]=val[idx]
    	return grid