"""
--------------------------------------------------------------------------------
File: Brute_Force.py
Problem: 0283. Move Zeroes
Link: https://leetcode.com/problems/move-zeroes/

Author: MD Saifullah Baig.A
Date: 06.01.2026

Description:
    This approach creates a temporary list to store non-zero elements.
    We then overwrite the original array with these elements and fill the 
    remaining positions with zeros.
    
    Time Complexity: O(N)
    Space Complexity: O(N) - Uses extra space (not in-place).
--------------------------------------------------------------------------------
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        non_zero=[]
        for num in nums:
            if num!=0:
                non_zero.append(num)
        for j in range(len(non_zero)):
            nums[j]=non_zero[j]
        for j in range(len(non_zero),len(nums)):
            nums[j]=0
        return nums
