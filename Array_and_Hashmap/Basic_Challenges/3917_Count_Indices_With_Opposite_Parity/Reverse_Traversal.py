class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        n=len(nums)
        result=[0]*n
        even=[]
        odd=[]
        for i in range(n-1,-1,-1):
            if nums[i]&1==1:
                odd.append(nums[i])
                result[i]=len(even)
            else:
                even.append(nums[i])
                result[i]=len(odd)
        return result