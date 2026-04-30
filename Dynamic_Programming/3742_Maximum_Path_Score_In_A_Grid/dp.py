class Solution:
    def maxPathScore(self,grid:List[List[int]],k:int)->int:
        if not grid or not grid[0]:return -1
        rows,cols=len(grid),len(grid[0])
        dp=[{} for _ in range(cols)]
        dp[0][k]=0
        for r in range(rows):
            for c in range(cols):
                val=grid[r][c]
                prev=dict(dp[c-1] if c>0 else {})
                for r_k,scr in dp[c].items():
                    if r_k not in prev or scr>prev[r_k]:prev[r_k]=scr
                nxt={}
                if val!=0:
                    for r_k,scr in prev.items():
                        if r_k>0:nxt[r_k-1]=scr+val
                else:nxt=prev
                dp[c]=nxt
        return max(dp[-1].values()) if dp[-1] else -1  