class Solution(object):
    def maxArea(self,h,w,horizontalCuts,verticalCuts):
    	horizontalCuts.sort()
    	verticalCuts.sort()
    	max_x=max(horizontalCuts[0],h-horizontalCuts[-1])
    	max_y=max(verticalCuts[0],w-verticalCuts[-1])
    	for i in range(1,len(horizontalCuts)):
    		max_x=max(max_x,horizontalCuts[i]-horizontalCuts[i-1])
    	for j in range(1,len(verticalCuts)):
    		max_y=max(max_y,verticalCuts[j]-verticalCuts[j-1])
    	area=max_x*max_y
    	return area%(10**9+7)