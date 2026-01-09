"""
--------------------------------------------------------------------------------
File: Optimal_Math_Approach.py
Problem: 1191. K-Concatenation Maximum Sum
Link: https://leetcode.com/problems/k-concatenation-maximum-sum/

Author: MD Saifullah Baig.A
Date: 09.01.2026

Description:
    This solution uses a mathematical approach combining Kadane's Algorithm 
    with Prefix/Suffix Sum analysis to achieve O(1) space complexity.

    1. Base Case (k=1): 
       We use standard Kadane's algorithm to find the max subarray sum within 
       a single array copy.

    2. Concatenation Case (k>1):
       - Internal Max: The best sum might still be inside one copy (Kadane's).
       - Crossing Max: The best sum might span across the boundary.
         We calculate this as: (Max Suffix of First Copy) + (Max Prefix of Second Copy).
         * Max Suffix is derived efficiently as: Total Sum - Min Prefix Sum.
       - If the Total Sum is positive, we include the (k-2) middle copies 
         to the Crossing Max.

    Time Complexity: O(N) - We traverse the array exactly once.
    Space Complexity: O(1) - We only use a few variables for tracking sums.
--------------------------------------------------------------------------------
"""
class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        limiter=10**9+7
        curr_prefix=0
        max_prefix=0
        min_prefix=0
        curr_sub=0
        max_sub=0
        total=0 
        for num in arr:
            curr_sub+=num
            if curr_sub<0:
                curr_sub=0
            max_sub=max(max_sub,curr_sub)
            curr_prefix+=num
            max_prefix=max(max_prefix,curr_prefix)
            min_prefix=min(min_prefix,curr_prefix)
        total=curr_prefix 
        if k==1:
            return max_sub%limiter
        max_suffix=total-min_prefix
        cross_sum=max_suffix+max_prefix
        if total>0:
            cross_sum+=(k-2)*total
        return max(max_sub, cross_sum)%limiter