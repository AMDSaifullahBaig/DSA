"""
--------------------------------------------------------------------------------
File: solution.py
Problem: 0567. Permutation in String
Link: https://leetcode.com/problems/permutation-in-string/

Author: MD Saifullah Baig.A
Date: 12.01.2026

Description:
    This module contains the "Sliding Window with Frequency Map" solution 
    for the Permutation in String problem. It utilizes Python's Counter class
    to maintain a running frequency count of characters in the current window,
    achieving O(N) time complexity by avoiding repetitive sorting.
--------------------------------------------------------------------------------
"""
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window=len(s1)
        secondary=Counter(s1)
        primary=Counter(s2[:window])
        l=0
        r=len(s1)-1
        while r<len(s2):
            if primary==secondary:
                return True
            r+=1
            if r<len(s2):
                primary[s2[r]]=primary.get(s2[r],0)+1
            primary[s2[l]]-=1
            l+=1
        return False