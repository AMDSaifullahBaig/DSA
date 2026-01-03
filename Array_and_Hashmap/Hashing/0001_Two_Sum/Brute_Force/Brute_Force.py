"""
--------------------------------------------------------------------------------
File: solution.py
Problem: 0001. Two Sum
Link: https://leetcode.com/problems/two-sum/

Author: MD Saifullah Baig.A
Date: 01.01.2026

Description:
    This module contains the [Approach Name, e.g., "Brute Force"] solution 
    for the Two Sum problem. It handles edge cases including duplicates and 
    negative numbers.
--------------------------------------------------------------------------------
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i,1+len(nums)):
                if target ==nums[i]+nums[j]:
                    return i,j