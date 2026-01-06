"""
--------------------------------------------------------------------------------
File: Two_Pointers.py
Problem: 0042. Trapping Rain Water
Link: https://leetcode.com/problems/trapping-rain-water/

Author: MD Saifullah Baig.A
Date: 05.01.2026

Description:
    This module contains the "Two Pointers" solution. It achieves O(1) space 
    efficiency by maintaining left and right pointers and processing the 
    shorter side dynamically.
--------------------------------------------------------------------------------
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n=len(height)
        l,r=0,n-1
        l_max,r_max=height[l],height[r]
        result=0
        while l<r:
            if height[l]<height[r]:
                if height[l]>l_max:
                    l_max=height[l]
                else:
                    result+=l_max-height[l]
                l+=1
            else:
                if height[r]>r_max:
                    r_max=height[r]
                else:
                    result+=r_max-height[r]
                r-=1
        return result