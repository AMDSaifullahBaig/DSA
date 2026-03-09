class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        c=0
        for i in nums:
            n=int(math.log10(i))+1
            if n&1!=1:
                c+=1
        return c