"""
--------------------------------------------------------------------------------
File: Optimized_Two_Pointers.py
Problem: 0011. Container With Most Water
Link: https://leetcode.com/problems/container-with-most-water/

Author: MD Saifullah Baig.A
Date: 04.01.2026

Description:
    This approach builds on the standard Two Pointers method. It optimizes execution 
    time by skipping over lines that are shorter than or equal to the current 
    edge, as they cannot possibly form a larger container with a smaller width.
    
    Time Complexity: O(N) (Faster runtime in practice)
    Space Complexity: O(1)
--------------------------------------------------------------------------------
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maximum=0
        l,r=0,len(height)-1
        while l<r:
            minimum=min(height[l],height[r])
            maximum=max(maximum,minimum*(r-l))
            if height[l]<height[r]:
                while (height[l]<=minimum) and l<r:
                    l+=1
            else:
                while (height[r]<=minimum) and l<r:
                    r-=1
        return maximum