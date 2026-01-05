"""
--------------------------------------------------------------------------------
File: Monotonic_Stack.py
Problem: 0042. Trapping Rain Water
Link: https://leetcode.com/problems/trapping-rain-water/

Author: MD Saifullah Baig.A
Date: 05.01.2026

Description:
    This module contains the "Monotonic Stack" solution. It uses a stack to 
    track decreasing heights and calculates water horizontally when a taller 
    boundary is encountered.
--------------------------------------------------------------------------------
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        stack=[]
        result=0
        for i in range(len(height)):
            while stack and height[stack[-1]]<height[i]:
                top=stack.pop()
                if not stack:
                    break
                left_end=stack[-1]
                width=i-left_end-1
                result+=width*(min(height[i],height[left_end])-height[top])
            stack.append(i)
        return result