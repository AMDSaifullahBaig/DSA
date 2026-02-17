class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        cache=[0]*len(nums)
        positive=0
        negetive=1
        for i in nums:
            if i>0:
                cache[positive]=i
                positive+=2
            else:
                cache[negetive]=i
                negetive+=2
        return cache