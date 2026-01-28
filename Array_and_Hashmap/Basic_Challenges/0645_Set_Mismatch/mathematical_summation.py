class Solution(object):
    def findErrorNums(self, nums):
        n=len(nums)
        summation=n*(n+1)//2
        duplicate=sum(nums)-sum(set(nums))
        missing=summation-sum(set(nums))
        return [duplicate,missing]
        