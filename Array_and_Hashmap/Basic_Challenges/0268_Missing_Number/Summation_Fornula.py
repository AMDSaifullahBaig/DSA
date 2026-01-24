class Solution(object):
    def missingNumber(self, nums):
        high=len(nums)
        summation=high*(high+1)/2
        summation-=sum(nums)
        return summation