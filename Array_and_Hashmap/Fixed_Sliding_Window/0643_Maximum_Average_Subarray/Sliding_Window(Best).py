"""
--------------------------------------------------------------------------------
File: Sliding_Window.py
Problem: 0643. Maximum Average Subarray I
Link: https://leetcode.com/problems/maximum-average-subarray-i/

Author: MD Saifullah Baig.A
Date: 10.01.2026

Description:
    This approach uses the Sliding Window technique to find the maximum average.
    
    Instead of recalculating the sum for every subarray (which takes O(N*k)),
    we maintain a running sum.
    
    1. Calculate the sum of the first 'k' elements.
    2. Slide the window one step at a time:
       - Subtract the element leaving the window (nums[i-k]).
       - Add the element entering the window (nums[i]).
    3. Update the maximum sum found so far.
    4. Finally, divide the max sum by 'k' to get the average.
    
    Time Complexity: O(N) - We iterate through the array exactly once.
    Space Complexity: O(1) - No extra data structures are used.
--------------------------------------------------------------------------------
"""

class Solution:     
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum=sum(nums[0:k])
        max_sum=curr_sum
        for i in range(k,len(nums)):
            curr_sum=curr_sum-nums[i-k]+nums[i]
            if curr_sum>max_sum:
                max_sum=curr_sum
        return max_sum/k