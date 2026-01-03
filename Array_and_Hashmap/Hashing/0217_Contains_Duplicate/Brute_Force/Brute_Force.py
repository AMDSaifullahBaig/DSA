"""
--------------------------------------------------------------------------------
File: Brute_Force.py
Problem: 0217. Contains Duplicate
Link: https://leetcode.com/problems/contains-duplicate/

Author: MD Saifullah Baig.A
Date: 02.01.2026

Description:
    This approach uses nested loops to compare every element with every other 
    element. It is the most intuitive but inefficient solution.
    
    Time Complexity: O(N^2)
    Space Complexity: O(1)
------
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in nums:
            for j in nums[1+i:]:
                if i==j :
                    return True
        return False