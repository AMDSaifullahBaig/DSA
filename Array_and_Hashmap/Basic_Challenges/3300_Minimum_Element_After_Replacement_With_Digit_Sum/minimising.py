class Solution:
    def minElement(self, nums: List[int]) -> int:
        minimum=10**4
        for i in range(len(nums)):
            c=0
            while nums[i]:
                c+=nums[i]%10
                nums[i]//=10
            minimum=min(minimum,c)
        return minimum