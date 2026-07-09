from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        
        # Collect non-zero digits and their original positions
        nz_vals = []
        nz_indices = []
        for i, char in enumerate(s):
            if char != '0':
                nz_vals.append(int(char))
                nz_indices.append(i)
                
        n = len(nz_vals)
        
        # Precompute prefix sums for the digit sum
        pref_sum = [0] * (n + 1)
        for i in range(n):
            pref_sum[i + 1] = pref_sum[i] + nz_vals[i]
            
        # Precompute prefix values for the concatenated integer x
        P = [0] * (n + 1)
        for i in range(n):
            P[i + 1] = (P[i] * 10 + nz_vals[i]) % MOD
            
        # Precompute powers of 10 modulo MOD
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD
            
        ans = []
        for l, r in queries:
            # Find the range [L, R] of non-zero elements completely within [l, r]
            L = bisect_left(nz_indices, l)
            R = bisect_right(nz_indices, r) - 1
            
            if L > R:
                ans.append(0)
            else:
                # 1. Compute the concatenated integer x modulo MOD
                x = (P[R + 1] - P[L] * pow10[R - L + 1]) % MOD
                
                # 2. Compute the digit sum
                digit_sum = pref_sum[R + 1] - pref_sum[L]
                
                # 3. Final answer for this query
                ans.append((x * digit_sum) % MOD)
                
        return ans