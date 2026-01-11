class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maximum=0
        curr=0
        for num in nums:
            if num==1:
                curr+=1
                if curr>maximum:
                    maximum=curr
            else:
                curr=0
        return maximum