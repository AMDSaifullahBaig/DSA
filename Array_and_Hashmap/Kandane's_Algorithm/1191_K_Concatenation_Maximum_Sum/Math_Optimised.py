"""
--------------------------------------------------------------------------------
File: Optimal_Math.py
Problem: 1191. K-Concatenation Maximum Sum
Link: https://leetcode.com/problems/k-concatenation-maximum-sum/

Author: MD Saifullah Baig.A
Date: 09.01.2026

Description:
    This approach uses a mathematical observation to avoid TLE/MLE:
    
    1. If k=1: The answer is just standard Kadane's on 'arr'.
    2. If k>1: The pattern stabilizes after 2 copies.
       - We run Kadane's on (arr * 2). This finds the best "Crossing Sum".
       - If the total sum of 'arr' is positive, we can include the (k-2) 
         middle copies to boost the score.
    
    Time Complexity: O(N)
    Space Complexity: O(N) (Only creates an array of size 2*N)
--------------------------------------------------------------------------------

"""
from typing import List
class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        limiter=10**9 + 7
        def kadane(nums):
            curr=0
            maximum=0
            for n in nums:
                curr=max(n,curr+n)
                maximum=max(maximum,curr)
            return maximum
        if k==1:
            return kadane(arr)
        double=kadane(arr*2)
        total=sum(arr)
        if total<0:
            return double%limiter
        else:
            return (double+total*(k-2))%limiter
