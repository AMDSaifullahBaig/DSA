class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        if len(piles)==h:return r
        result=0
        while l<=r:
            m=(l+r)//2
            total=0
            for i in piles:
                total+=ceil(i/m)
            if total<=h:
                result=m
                r=m-1
            else:
                l=m+1
        return result