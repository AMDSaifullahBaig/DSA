class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        def solve(i,n):
        	if i<0 or i>=n or check[i]:
        		return False
        	if arr[i]==0:
        		return True
        	check[i]=True
        	l=i-arr[i]
        	r=i+arr[i]
        	return solve(r,n) or solve(l,n)
        check=[False]*len(arr)
        return solve(start,len(arr))