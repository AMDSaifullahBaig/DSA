class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        result=[0]*n
        stack=[]
        for idx in range(n):
            while stack and temperatures[idx]>stack[-1][0]:
                i,j=stack.pop()
                result[j]=idx-j
            stack.append((temperatures[idx],idx))
        return result