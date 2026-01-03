"""
--------------------------------------------------------------------------------
File: Frequency_Counter.py
Problem: 0242. Valid Anagram
Link: https://leetcode.com/problems/valid-anagram/

Author: MD Saifullah Baig.A
Date: 03.01.2026

Description:
    This approach utilizes Python's built-in `collections.Counter` to create 
    frequency maps for both strings in a concise, readable manner.
    
    Time Complexity: O(N)
    Space Complexity: O(N)
--------------------------------------------------------------------------------
"""
from collections import Counter
class Solution():
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        return Counter(s)==Counter(t)