"""
--------------------------------------------------------------------------------
File: solution.py
Problem: 0001. Two Sum
Link: https://leetcode.com/problems/two-sum/

Author: MD Saifullah Baig.A
Date: 01.01.2026

Description:
    This module contains the [Approach Name, e.g., "One Pass Hash map"] solution 
    for the Two Sum problem. It handles edge cases including duplicates and 
    negative numbers.
--------------------------------------------------------------------------------
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash={}
        for idx,num in enumerate(nums):
            complement=target-num
            if complement in hash:
                return [hash[target-num],idx]
            hash[num]=idx
        return []