"""
--------------------------------------------------------------------------------
File: Dynamic_Programming.py
Problem: 0042. Trapping Rain Water
Link: https://leetcode.com/problems/trapping-rain-water/

Author: MD Saifullah Baig.A
Date: 05.01.2026

Description:
    This module contains the "Dynamic Programming" solution. It optimizes the 
    Brute Force approach by pre-computing the left and right maximum heights 
    into arrays to avoid repeated scanning.
--------------------------------------------------------------------------------
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:return 0

        n=len(height)
        l_max=[0]*n
        r_max=[0]*n

        l_max[0]=height[0]
        r_max[n-1]=height[n-1]

        for i in range(1,n):
            l_max[i]=max(l_max[i-1],height[i])
        
        for i in range(n-2,-1,-1):
            r_max[i]=max(r_max[i+1],height[i])

        result=0
        for i in range(n):
            result+=min(l_max[i],r_max[i])-height[i]
        return result