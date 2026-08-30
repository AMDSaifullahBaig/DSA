class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        n=len(heights)
        stack=[]
        maximum=0
        for i in range(n):
            while stack and heights[i]<heights[stack[-1]]:
                h=heights[stack.pop()]
                if not stack:
                    w=i
                else:
                    w=i-stack[-1]-1
                if w*h>maximum:
                    maximum=w*h
            stack.append(i)
        return maximum