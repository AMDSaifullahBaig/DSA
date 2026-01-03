"""
--------------------------------------------------------------------------------
File: Hash_Map.py
Problem: 0242. Valid Anagram
Link: https://leetcode.com/problems/valid-anagram/

Author: MD Saifullah Baig.A
Date: 03.01.2026

Description:
    This approach uses two Hash Maps (or Dictionaries) to count the frequency 
    of each character in both strings. We then compare the counts.
    
    Time Complexity: O(N) - We iterate through the strings once.
    Space Complexity: O(N) - To store the character counts (technically O(26) ~ O(1)).
--------------------------------------------------------------------------------
"""
class Solution():
    def isAnagram(self, s: str, t: str) -> bool:
        hash={}
        if len(s)!=len(t):
            return False
        for i in s:
            hash[i]=hash.get(i,0)+1
        for j in t:
            if j not in hash:
                return False
            hash[j]-=1
            if hash[j]<0:
                return False
        return True