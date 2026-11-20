class Solution:
    def countConsistent(self, nums: list[int]) -> int:
        result=len(nums)
        for i in range(len(nums)):
            curr=nums[i]
            minimum=nums[i]
            for j in range(i+1,len(nums)):
                curr&=nums[j]
                minimum=min(minimum,nums[j])
                if curr==minimum:
                    result+=1
        return result