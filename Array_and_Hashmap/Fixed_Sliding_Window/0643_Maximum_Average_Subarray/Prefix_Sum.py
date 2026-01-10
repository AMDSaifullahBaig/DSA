"""
--------------------------------------------------------------------------------
File: Prefix_Sum.py
Problem: 0643. Maximum Average Subarray I
Link: https://leetcode.com/problems/maximum-average-subarray-i/

Author: MD Saifullah Baig.A
Date: 10.01.2026

Description:
    This approach uses the Prefix Sum technique (Cumulative Sum).
    
    1. Pre-process the array to create a 'prefix' array where prefix[i]
       contains the sum of nums[0]...nums[i].
    2. To find the sum of a window ending at index 'i' with length 'k',
       we use the formula: WindowSum = Prefix[i] - Prefix[i-k].
       
    This allows us to calculate any window sum in O(1) time after O(N) preprocessing.
    
    Time Complexity: O(N) - Two passes (one to build prefix, one to scan).
    Space Complexity: O(N) - Uses extra space for the prefix array.
--------------------------------------------------------------------------------
"""
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        prefix=[0]*len(nums)
        prefix[0]=nums[0]
        for i in range(1,len(nums)):
            prefix[i]=prefix[i-1]+nums[i]
        max_sum=prefix[k-1]
        for i in range(k,len(nums)+1):
            window=prefix[i]-prefix[i-k]
            if window>max_sum:
                max_sum=window
        return max_sum/k