"""
--------------------------------------------------------------------------------
File: Brute_Force.py
Problem: 1191. K-Concatenation Maximum Sum
Link: https://leetcode.com/problems/k-concatenation-maximum-sum/

Author: MD Saifullah Baig.A
Date: 09.01.2026

Description:
    This approach literally concatenates the array 'k' times and runs 
    Kadane's Algorithm on the massive result.
    
    WARNING: 
    - This will fail with Memory Limit Exceeded (MLE) for large k.
    - Time Complexity: O(N * K)
    - Space Complexity: O(N * K)
--------------------------------------------------------------------------------
"""
class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        val=10**9+7
        array=arr*k
        curr=0
        maximum=0
        for i in array:
            curr=max(i,curr+i)
            maximum=max(maximum,curr)
        return maximum%val