"""
--------------------------------------------------------------------------------
File: Brute_Force.py
Problem: 0042. Trapping Rain Water
Link: https://leetcode.com/problems/trapping-rain-water/

Author: MD Saifullah Baig.A
Date: 05.01.2026

Description:
    This module contains the "Brute Force" solution for the Trapping Rain Water 
    problem. It iterates through each bar and finds the maximum height to its 
    left and right to calculate trapped water.
--------------------------------------------------------------------------------
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        result=0
        for i in range(1,n-1):
            max_l=max_r=0
            for l in range(i):
                max_l=max(max_l,height[l])
            for r in range(i+1,n):
                max_r=max(max_r,height[r])
            water=min(max_l,max_r)-height[i]
            if water>0:
                result+=water
        return result