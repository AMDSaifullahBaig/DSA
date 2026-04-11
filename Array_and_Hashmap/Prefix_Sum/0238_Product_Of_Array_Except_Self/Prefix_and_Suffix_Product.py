class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=[1]
        for i in range(1,len(nums)):
            result.append(result[i-1]*nums[i-1])
        prod=nums[-1]
        for i in range(len(nums)-2,-1,-1):
            result[i]*=prod
            prod*=nums[i]
        return result