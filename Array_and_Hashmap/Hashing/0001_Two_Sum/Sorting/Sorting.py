"""
--------------------------------------------------------------------------------
File: solution.py
Problem: 0001. Two Sum
Link: https://leetcode.com/problems/two-sum/

Author: MD Saifullah Baig.A
Date: 01.01.2026

Description:
    This module contains the [Approach Name, e.g., "Sorting - Two Pointer"] solution 
    for the Two Sum problem. It handles edge cases including duplicates and 
    negative numbers.
--------------------------------------------------------------------------------
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_sorted=[(value,idx) for idx,value in enumerate(nums)]
        nums_sorted.sort()
        left,right=0,len(nums)-1
        while (left<right):
            sum=nums_sorted[left][0]+nums_sorted[right][0]
            if sum==target:
                return nums_sorted[left][1],nums_sorted[right][1]
            elif sum>target:
                right-=1
            elif sum<target:
                left+=1
        return []