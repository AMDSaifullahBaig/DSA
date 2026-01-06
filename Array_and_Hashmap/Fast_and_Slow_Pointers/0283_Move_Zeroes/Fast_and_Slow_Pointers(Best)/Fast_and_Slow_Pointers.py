"""
--------------------------------------------------------------------------------
File: Two_Pointers.py
Problem: 0283. Move Zeroes
Link: https://leetcode.com/problems/move-zeroes/

Author: MD Saifullah Baig.A
Date: 06.01.2026

Description:
    This approach uses the "Slow and Fast Pointers" technique (Partitioning).
    - 'l' (left) pointer tracks the position of the next non-zero element.
    - 'r' (right) pointer iterates through the array.
    
    When we find a non-zero element at 'r', we SWAP it with the element at 'l'.
    This pushes non-zeros to the front and zeros to the back simultaneously 
    in a single pass.
    
    Time Complexity: O(N)
    Space Complexity: O(1)
--------------------------------------------------------------------------------
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i,j=0,0
        for j in range(len(nums)):
            if nums[j]!=0:
                nums[j],nums[i]=nums[i],nums[j]
                i+=1
        return nums