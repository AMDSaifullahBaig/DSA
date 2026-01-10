"""
--------------------------------------------------------------------------------
File: Brute_Force.py
Problem: 0643. Maximum Average Subarray I
Link: https://leetcode.com/problems/maximum-average-subarray-i/

Author: MD Saifullah Baig.A
Date: 10.01.2026

Description:
    This approach uses a Brute Force strategy to find the maximum average.
    
    It iterates through every possible starting position of a subarray of length 'k'.
    For each position, it calculates the sum of the next 'k' elements from scratch.
    
    While logic is simple, this approach is inefficient for large 'k' because
    it repeatedly sums overlapping elements.
    
    Time Complexity: O(N * k) - Nested loops cause repeated work.
                                Can lead to Time Limit Exceeded (TLE).
    Space Complexity: O(1) - No extra data structures are used.
--------------------------------------------------------------------------------
"""
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum=float('-inf')
        for i in range(len(nums)-k+1):
            curr=0
            for j in range (i,k+i):
                curr+=nums[j]
            max_sum=max(max_sum,curr)
        return max_sum/k