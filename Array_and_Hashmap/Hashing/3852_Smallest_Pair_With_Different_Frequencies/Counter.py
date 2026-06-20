class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        c=Counter(nums)
        x=min(c.keys())
        y=math.inf
        for i in c.keys():
            if i!=x and c[i]!=c[x]:
                if i<y:
                   y=i
        return [x,y] if y!=math.inf else [-1, -1]