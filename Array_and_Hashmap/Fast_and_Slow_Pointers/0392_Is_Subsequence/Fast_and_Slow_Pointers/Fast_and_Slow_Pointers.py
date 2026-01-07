"""
--------------------------------------------------------------------------------
File: Two_Pointers.py
Problem: 0392. Is Subsequence
Link: https://leetcode.com/problems/is-subsequence/

Author: MD Saifullah Baig.A
Date: 07.01.2026

Description:
    This approach uses two pointers to traverse both strings 's' and 't'.
    - Pointer 'i' tracks our progress in 's' (the subsequence we want to find).
    - Pointer 'j' iterates through 't' (the source string).
    
    If characters match (s[i] == t[j]), we move 'i' forward.
    We always move 'j' forward.
    
    If 'i' reaches the end of 's', it means we found all characters in order.
    
    Time Complexity: O(T) - We iterate through 't' once.
    Space Complexity: O(1) - Constant extra space.
--------------------------------------------------------------------------------
"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        if not s:
            return True
        for j in t:
            if i<len(s) and s[i]==j:
                i+=1
        return i==len(s)