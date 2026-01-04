"""
--------------------------------------------------------------------------------
File: Two_Pointers.py
Problem: 0011. Container With Most Water
Link: https://leetcode.com/problems/container-with-most-water/

Author: MD Saifullah Baig.A
Date: 04.01.2026

Description:
    This approach uses two pointers starting at both ends of the array. At each 
    step, we calculate the area and greedily move the pointer pointing to the 
    shorter line inward, hoping to find a taller line.
    
    Time Complexity: O(N)
    Space Complexity: O(1)
--------------------------------------------------------------------------------
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maximum=0
        l,r=0,len(height)-1
        while l<r:
            curr=min(height[l],height[r])*(r-l)
            maximum=max(maximum,curr)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return maximum

