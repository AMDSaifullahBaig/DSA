"""
--------------------------------------------------------------------------------
File: solution.py
Problem: 0567. Permutation in String
Link: https://leetcode.com/problems/permutation-in-string/

Author: MD Saifullah Baig.A
Date: 12.01.2026

Description:
    This module contains the "Sorting with Sliding Window" solution for the 
    Permutation in String problem. It iterates through the string 's2' using 
    a window of size 's1', sorting the characters in each window to check 
    for an exact match with the sorted 's1'.
--------------------------------------------------------------------------------
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length=len(s1)
        target = sorted(s1)
        for i in range(len(s2)-length+1):
            window=s2[i:i+length]
            if sorted(window)==target:
                return True