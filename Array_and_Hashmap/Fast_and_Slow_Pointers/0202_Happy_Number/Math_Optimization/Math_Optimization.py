"""
--------------------------------------------------------------------------------
File: Math_Approach.py
Problem: 0202. Happy Number
Link: https://leetcode.com/problems/happy-number/

Author: MD Saifullah Baig.A
Date: 07.01.2026

Description:
    This approach relies on a mathematical property of Happy Numbers.
    Any number that is NOT happy will eventually fall into the specific cycle:
    4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4.
    
    Instead of tracking all numbers, we simply check:
    - If n reaches 1: Return True.
    - If n reaches 4: Return False (we know it's trapped in the cycle).
    
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
                num=num//10
                sum+=digit**2
            return sum
        while n!=1 and n!=4:
            n=next(n)
        return n==1
