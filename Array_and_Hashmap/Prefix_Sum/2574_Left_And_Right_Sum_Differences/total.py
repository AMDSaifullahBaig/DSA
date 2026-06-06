class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total=sum(nums)
        l=0
        result=[]   
        for i in nums:
            r=total-l-i
            result.append(abs(l-r))
            l+=i
        return result