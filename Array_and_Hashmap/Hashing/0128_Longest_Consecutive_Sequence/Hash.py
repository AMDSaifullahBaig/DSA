class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash=set(nums)
        maximum=0
        for i in hash:
            if i-1 not in hash:
                curr=i
                length=1
                while curr+1 in hash:
                	curr+=1
                	length+=1
                maximum=max(maximum,length)
        return maximum