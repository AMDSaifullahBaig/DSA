"""
--------------------------------------------------------------------------------
File: Hashing.py
Problem: 0217. Contains Duplicate
Link: https://leetcode.com/problems/contains-duplicate/

Author: MD Saifullah Baig.A
Date: 02.01.2026

Description:
    This is the OPTIMAL approach. It uses a Hash Set to track seen elements.
    Lookups in a set are O(1) on average, making this extremely fast.
    
    Time Complexity: O(N)
    Space Complexity: O(N)
--------------------------------------------------------------------------------
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_set=set()
        for i in nums:
            if i in hash_set:
                return True
            hash_set.add(i)
        return False