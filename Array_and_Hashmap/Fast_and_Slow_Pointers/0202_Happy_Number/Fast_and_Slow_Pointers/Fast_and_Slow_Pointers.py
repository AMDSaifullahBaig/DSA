"""
--------------------------------------------------------------------------------
File: Fast_Slow_Pointers.py
Problem: 0202. Happy Number
Link: https://leetcode.com/problems/happy-number/

Author: MD Saifullah Baig.A
Date: 07.01.2026

Description:
    This approach uses the "Fast and Slow Pointers" technique to detect cycles
    without using extra memory for a Hash Set.
    
    - 'slow' pointer computes the sum of squares once per step.
    - 'fast' pointer computes the sum of squares twice per step.
    
    If 'fast' reaches 1, the number is Happy.
    If 'fast' catches up to 'slow' (and it's not 1), we are in a loop -> False.
    
    Time Complexity: O(log N)
    Space Complexity: O(1)
--------------------------------------------------------------------------------
"""
class Solution:
    def isHappy(self, n: int) -> bool:
        def next(num:int)->int:
            sum=0
            while num:
                digit=num%10
                num//=10
                sum+=digit**2
            return sum
        fast=next(n)
        slow=n
        while fast!=1 and fast!=4 and slow!=fast:
            slow=next(slow)
            fast=next(next(fast))
        return fast==1