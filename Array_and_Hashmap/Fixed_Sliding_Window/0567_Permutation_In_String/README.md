# 0567. Permutation in String

| **Author** | **Last Updated** | **Difficulty** | **Tags** |
| :--- | :--- | :--- | :--- |
| MD Saifullah Baig.A | 12.01.2026 | 🟡 Medium | Hash Table, Two Pointers, String, Sliding Window |

**Problem Link:** [LeetCode 0567](https://leetcode.com/problems/permutation-in-string/)

---

## 📂 Quick Access
| Approach | Time Complexity | Space Complexity | Code Link |
| :--- | :--- | :--- | :--- |
| **1. Sorting (The Trap)** | $O(N \cdot M \log M)$ | $O(M)$ | [📄 View Solution](./Sorting.py) |
| **2. Hash Map Window** | $O(N)$ | $O(1)$ | [📄 View Solution](./Hashing_and_Sliding_Window.py) |

---

## 1. Problem Statement

Given two strings `s1` and `s2`, return `true` if `s2` contains a permutation of `s1`, or `false` otherwise.

In other words, return `true` if one of `s1`'s permutations is the substring of `s2`.

**Example 1:**
```text
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
```
## 2. Approach Analysis
### 🐌 Approach 1: Sorting Window (The Trap)
Most beginners try this first. We iterate through s2, and for every substring, we sort it to see if it matches sorted(s1).
+ Logic: 
    - if sorted(window) == sorted(target): return True
    - Why it is slow: 
        + Sorting takes $M \log M$. 
        + Doing this inside a loop of size $N$ results in a huge performance hit.
- Status: Passes small test cases, but fails or runs very slow on large inputs.
### 🚀 Approach 2: Sliding Window + Fixed Array (Optimal)
Instead of sorting, we simply count. Anagrams have the exact same character counts.
+ Sliding Logic:Add the new character entering the window: window[new_char] += 1
+ Remove the old character leaving the window: window[old_char] -= 1
+ Compare: if s1_counts == window_counts: return TruePros: Strict $O(N)$ linear time.
+ Comparing is effectively $O(1)$.
## 3. 📂 Project Structure:
```text
DSA/
├── Sliding_Window/
│   └── 0567_Permutation_in_String/      
│       │
│       │Sorting_Window.py       # O(N*K log K) Solution
│       │
│       │HashMap_Window.py       # Python Counter Solution
│       │
│       ├── assets/
│       │   ├── Efficiency_graph.png
│       │   └── Submission_Results.png
│       │
│       └── README.md
```
## 4. 📊 Efficiency Comparison
> **Note:** The graph below compares the runtime of the Sorting approach ($O(N \log N)$) vs. the Sliding Window approach ($O(N)$).

![Efficiency Graph.Check assets](./assets/Efficiency_graph.png)

---

## 5. 🏆 LeetCode Submission

![Submission Result.Check assets](./assets/Submission_Results.png)