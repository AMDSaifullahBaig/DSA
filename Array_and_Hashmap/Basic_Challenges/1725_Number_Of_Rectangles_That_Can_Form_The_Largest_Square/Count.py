class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        result=[]
        for i in rectangles:
            result.append(min(i))
        return result.count(max(result))