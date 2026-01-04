"""
--------------------------------------------------------------------------------
File: Brute_Force.py
Problem: 0011. Container With Most Water
Link: [https://leetcode.com/problems/container-with-most-water/](https://leetcode.com/problems/container-with-most-water/)

Author: MD Saifullah Baig.A
Date: 04.01.2026

Description:
    This approach uses nested loops to calculate the area for every possible pair 
    of lines in the array and finds the maximum.
    
    Time Complexity: O(N^2)
    Space Complexity: O(1)
--------------------------------------------------------------------------------
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maximum=0
        n=len(height)
        for i in range(n):
            for j in range(i+1,n):
                minimum=min(height[i],height[j])
                w=j-i
                maximum=max(w*minimum,maximum)
        return maximum

