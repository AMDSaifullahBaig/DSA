"""
--------------------------------------------------------------------------------
File: Fixed_Array.py
Problem: 0242. Valid Anagram
Link: https://leetcode.com/problems/valid-anagram/

Author: MD Saifullah Baig.A
Date: 03.01.2026

Description:
    This approach uses a fixed-size integer array of length 26 (for 'a' to 'z').
    We increment counts for string 's' and decrement for string 't'. 
    If the array returns to all zeros, they are anagrams.
    
    Time Complexity: O(N)
    Space Complexity: O(1) - The array size (26) is constant regardless of input size.
--------------------------------------------------------------------------------
"""
class Solution():
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        array=[0]*26
        for i in range(len(s)):
            array[ord(s[i])-ord('a')]+=1
            array[ord(t[i])-ord('a')]-=1
        for i in array:
            if i!=0:
                return False
        return True