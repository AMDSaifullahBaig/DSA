"""
--------------------------------------------------------------------------------
File: Hash_Set.py
Problem: 0202. Happy Number
Link: https://leetcode.com/problems/happy-number/

Author: MD Saifullah Baig.A
Date: 07.01.2026

Description:
    This approach simulates the process of squaring digits and summing them.
    To detect infinite cycles, we store every number we encounter in a Hash Set.
    
    - If we reach 1: Return True (Happy).
    - If we see a number already in the set: We are in a loop -> Return False.
    
    Time Complexity: O(log N)
    Space Complexity: O(log N) - Stores history of numbers in the set.
--------------------------------------------------------------------------------
"""
class Solution:
    def isHappy(self, n: int) -> bool:
        hash_set=set()
        while n not in hash_set:
            hash_set.add(n)
            sum=0
            while n>0:
                digit=n%10
                sum+=digit**2
                n//=10
            if sum==1:
                return True
            n=sum
        return False