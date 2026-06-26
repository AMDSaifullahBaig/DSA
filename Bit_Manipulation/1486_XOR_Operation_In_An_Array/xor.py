class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        result=0
        nums=[]
        for i in range(n):
        	nums.append(start+i*2)
        for i in nums:
            result^=n
        return result   