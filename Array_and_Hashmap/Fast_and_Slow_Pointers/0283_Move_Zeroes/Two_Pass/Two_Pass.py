"""
--------------------------------------------------------------------------------
File: Two_Pass.py
Problem: 0283. Move Zeroes
Link: https://leetcode.com/problems/move-zeroes/

Author: MD Saifullah Baig.A
Date: 06.01.2026

Description:
    This approach uses two separate passes (iterations) over the array.
    1. First Pass: Move all non-zero elements to the front of the array by 
       overwriting indices.
    2. Second Pass: Fill all remaining indices (from the end of non-zeros) with 0.
    
    Time Complexity: O(N) - We iterate through the array twice.
    Space Complexity: O(1) - Done in-place.
--------------------------------------------------------------------------------
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        idx=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[idx]=nums[i]
                idx+=1
        for i in range(idx,len(nums)):
            nums[i]=0
        return nums