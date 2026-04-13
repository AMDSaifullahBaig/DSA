class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        minimum=len(nums)-1
        for i in range(len(nums)):
            if nums[i]==target:
                minimum=min(minimum,abs(start-i))
        return minimum