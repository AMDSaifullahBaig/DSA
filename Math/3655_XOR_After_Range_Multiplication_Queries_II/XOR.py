class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        MOD = 10**9 + 7
        threshold = int(n**0.5)
        small_k_queries = [[] for _ in range(threshold)]
        for l, r, k, v in queries:
            if v == 1: continue
            if k >= threshold:
                for i in range(l, r + 1, k):
                    nums[i] = (nums[i] * v) % MOD
            else:
                small_k_queries[k].append((l, r, v))
        for k in range(1, threshold):
            if not small_k_queries[k]:
                continue
            diff = [1] * (n + k + 1)
            for l, r, v in small_k_queries[k]:
                diff[l] = (diff[l] * v) % MOD
                last_idx = l + ((r - l) // k + 1) * k
                inv_v = pow(v, MOD - 2, MOD)
                diff[last_idx] = (diff[last_idx] * inv_v) % MOD
            for i in range(n):
                if i >= k:
                    diff[i] = (diff[i] * diff[i-k]) % MOD
                if diff[i] != 1:
                    nums[i] = (nums[i] * diff[i]) % MOD
        res = 0
        for x in nums:
            res ^= x
        return res