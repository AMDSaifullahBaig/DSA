# 1191. K-Concatenation Maximum Sum

| **Author** | **Last Updated** | **Difficulty** | **Tags** |
| :--- | :--- | :--- | :--- |
| MD Saifullah Baig.A | 09.01.2026 | 🟡 Medium | Array, Dynamic Programming, Greedy |

**Problem Link:** [LeetCode 1191](https://leetcode.com/problems/k-concatenation-maximum-sum/)

---

## 📂 Quick Access
| Approach | Time Complexity | Space Complexity | Code Link |
| :--- | :--- | :--- | :--- |
| **1. Simulation** | $O(N)$ | $O(N)$ | [📄 View Solution](./Brute_Force.py) |
| **2. Optimal Math** | $O(N)$ | $O(1)$ | [📄 View Solution](./Kadane_Algorithm_Optimised_2(Best).py) |

<br>

> **Recommended:** Approach 2 (Optimal Math) is the most efficient solution ($O(1)$ space) and avoids creating large arrays.

---

## 1. Problem Statement

Given an integer array `arr` and an integer `k`, modify the array by repeating it `k` times. For example, if `arr = [1, 2]` and `k = 3` then the modified array will be `[1, 2, 1, 2, 1, 2]`.

Return the **maximum sub-array sum** in the modified array. Note that the length of the sub-array can be `0` and its sum in that case is `0`.

*As the answer can be very large, return it modulo $10^9 + 7$.*

**Example 1:**
```text
Input: arr = [1, -2, 1], k = 5
Output: 2
Explanation: The subarray [1, 1] has the largest sum 2 (crossing the boundary).
```
## 2. Approach Analysis
### 📊 Complexity Analysis

| Approach | Time Complexity | Space Complexity | Key Idea |
| :--- | :--- | :--- | :--- |
| **Simulation** | $O(N)$ | $O(N)$ | Create `arr * 2` to physically simulate the boundary crossing. |
| **Optimal Math** | $O(N)$ | $O(1)$ | **Optimal.** Calculates `Max Suffix` + `Max Prefix` mathematically. |### ### 🐢 Approach 1: Simulation (Concatenation)
This approach physically creates a larger array to simulate the "boundary crossing" effect.
+ Logic:
    + If $k=1$, run Kadane on arr.
    + If $k > 1$, create a new array double_arr = arr * 2.
    + Run Kadane's Algorithm on double_arr.
    + If the total sum of arr is positive, add $(k-2) * total$ to the result.
+ Why it works:The maximum subarray can technically span more than 2 arrays only if the total sum is positive. 
+ Otherwise, checking 2 copies is sufficient to find any crossing pattern
+ Drawback: It requires $O(N)$ extra space to hold the doubled array.
### 🚀 Approach 2: Optimal Math (Prefix/Suffix)
This approach uses geometric logic to avoid creating any new lists, achieving $O(1)$ space.
+ Core Logic:The max sum is the maximum of:
    + Internal Max: The max subarray inside a single copy (Standard Kadane).
    + Crossing Max: The best sum crossing the boundary.
    $$CrossingSum = MaxSuffix + MaxPrefix$$
    $$(Where \ MaxSuffix = TotalSum - MinPrefix)$$
    + Spanning Max: If total > 0, we take the Crossing Max and fill the middle with all full copies:
    $$Spanning = CrossingSum + (k-2) \times TotalSum$$
## 3. 📂 Project Structure
```text
DSA/
├── Arrays/
│   └── 1191_K_Concatenation_Max_Sum/
│       |
│       │───Simulation_Approach.py     # O(N) Space Solution (arr*2)
│       │
│       │───Optimal_Math.py            # O(1) Space Solution
│       │
│       │───Efficiency_Benchmark.py    # Benchmarking Script
│       │
│       ├── assets/
│       │   ├── efficiency_graph.png
│       │   └── Submission_Results.png
│       │
│       └── README.md
```
### 4. 📊 Efficiency Comparison
The graph below compares the runtime and memory usage. Note that while both are $O(N)$ in time, the simulation approach uses significantly more memory (Orange line) compared to the Math approach (Green line).

![Efficiency Graph.Check assets](./assets/Efficiency_Graph.png)

### 5. 🏆 LeetCode Submission
Proof of the optimal solution passing 100% of test cases.

![Submission Result.Check assets](./assets/Submission_Results.png)