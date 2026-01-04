"""
--------------------------------------------------------------------------------
File: Hash_Length_Comparision.py
Problem: 0217. Contains Duplicate
Link: https://leetcode.com/problems/contains-duplicate/

Author: MD Saifullah Baig.A
Date: 02.01.2026

Description:
    A concise, Pythonic one-liner. Since Sets contain only unique elements,
    if the length of the set is smaller than the length of the list, 
    duplicates must exist.
    
    Time Complexity: O(N)
    Space Complexity: O(N)
--------------------------------------------------------------------------------
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return True if len(nums)>len(set(nums)) else False
    