class Solution:
    def arraySign(self, nums: List[int]) -> int:
        sign=1
        for i in nums:sign*=i
        if (sign>0):
            return 1
        elif (sign<0):
            return -1
        elif (sign==0):
            return 0