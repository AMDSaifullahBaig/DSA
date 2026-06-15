class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        actual=sorted(heights)
        c=0
        for i in range(len(heights)):
            if actual[i]!=heights[i]:
                c+=1
        return c