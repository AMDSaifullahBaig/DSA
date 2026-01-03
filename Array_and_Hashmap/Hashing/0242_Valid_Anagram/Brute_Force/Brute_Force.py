"""
--------------------------------------------------------------------------------
File: Sorting.py
Problem: 0242. Valid Anagram
Link: https://leetcode.com/problems/valid-anagram/

Author: MD Saifullah Baig.A
Date: 03.01.2026

Description:
    This approach sorts both strings and compares them. If they are anagrams, 
    they will be identical after sorting.
    
    Time Complexity: O(N log N) - Dominated by the sorting algorithm.
    Space Complexity: O(1) or O(N) - Depends on the sorting implementation.
--------------------------------------------------------------------------------
"""
class Solution():
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        return sorted(s)==sorted(t)