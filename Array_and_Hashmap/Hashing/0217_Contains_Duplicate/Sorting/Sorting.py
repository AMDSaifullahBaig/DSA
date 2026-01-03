"""
--------------------------------------------------------------------------------
File: Sorting.py
Problem: 0217. Contains Duplicate
Link: https://leetcode.com/problems/contains-duplicate/

Author: MD Saifullah Baig.A
Date: 02.01.2026

Description:
    This approach sorts the array first. If there are duplicates, they will be 
    adjacent to each other. We iterate once to check neighbors.
    
    Time Complexity: O(N log N)
    Space Complexity: O(1) (depending on sort implementation)
--------------------------------------------------------------------------------
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                return True
        return False