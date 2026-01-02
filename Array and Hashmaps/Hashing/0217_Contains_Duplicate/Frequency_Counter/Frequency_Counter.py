"""
--------------------------------------------------------------------------------
File: Frequency_Counter.py
Problem: 0217. Contains Duplicate
Link: https://leetcode.com/problems/contains-duplicate/

Author: MD Saifullah Baig.A
Date: 02.01.2026

Description:
    This approach uses Python's `collections.Counter` to build a frequency map 
    of all elements. We then check if any element appears more than once.
    
    Time Complexity: O(N)
    Space Complexity: O(N)
--------------------------------------------------------------------------------
"""
from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count=Counter(nums)
        for i in count.values():
            if i>1:
                return True
        return False
