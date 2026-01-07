"""
--------------------------------------------------------------------------------
File: Follow_Up_Binary_Search.py
Problem: 0392. Is Subsequence
Link: https://leetcode.com/problems/is-subsequence/

Author: MD Saifullah Baig.A
Date: 07.01.2026

Description:
    This approach is optimized for the "Follow-up" scenario where there are 
    many incoming 's' strings.
    
    1. Preprocessing: Store indices of each char in 't' in a Hash Map.
       Example: t = "bahbgd" -> {'b': [0, 3], 'a': [1], 'h': [2], 'g': [4], ...}
    
    2. Query: For each char in 's', use Binary Search (bisect_right) to find 
       the smallest valid index in 't' that is GREATER than the previous index.
    
    Time Complexity: O(S * log T) per query. (Processing 't' takes O(T) once).
    Space Complexity: O(T) to store the index map.
--------------------------------------------------------------------------------
"""
from collections import defaultdict
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        def binary_search(arr:list[int],target:int)->int:
            left=0
            right=len(arr)
            while left<right:
                middle=(left+right)//2
                if arr[middle]<=target:
                    left=middle+1
                else:
                    right=middle
            return left
        indices = defaultdict(list)
        for idx,char in enumerate(t):
            indices[char].append(idx)
        prev=-1
        for char in s:
            if char not in indices:
                return False
            pos=binary_search(indices[char],prev)
            if pos==len(indices[char]):
                return False
            prev=indices[char][pos]
        return True