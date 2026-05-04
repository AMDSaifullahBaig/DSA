class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        x0,y0=points[0]
        x1,y1=points[1]
        x2,y2=points[2]
        return (y1-y0)*(x2-x1)!=(y2-y1)*(x1-x0)