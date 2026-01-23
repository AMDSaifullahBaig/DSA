class Solution(object):
    def thirdMax(self, nums):
        hash=set(nums)
        hash=sorted(hash)
        if len(hash)>=3:
            return hash[-3]
        else:
            return hash[-1]