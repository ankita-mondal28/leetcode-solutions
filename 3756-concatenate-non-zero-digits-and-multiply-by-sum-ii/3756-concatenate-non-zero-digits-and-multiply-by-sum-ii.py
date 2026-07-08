class Solution:
    def sumAndMultiply(self, s: str, queries: list[list[int]]) -> list[int]:
        n = len(s)
        MOD = 10**9 + 7
        
        # Prefixes arrays: size n + 1 to handle l-1 = -1 cleanly
        prefix_sum = [0] * (n + 1)       # Cumulative sum of digits
        prefix_nonzero = [0] * (n + 1)   # Cumulative count of non-zero digits
        prefix_val = [0] * (n + 1)       # Cumulative concatenated value mod MOD
        
        # Precompute powers of 10 mod 10^9 + 7
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD
            
        # Build the prefix tables
        for i in range(n):
            d = int(s[i])
            prefix_sum[i + 1] = prefix_sum[i] + d
            
            if d != 0:
                prefix_nonzero[i + 1] = prefix_nonzero[i] + 1
                prefix_val[i + 1] = (prefix_val[i] * 10 + d) % MOD
            else:
                prefix_nonzero[i + 1] = prefix_nonzero[i]
                prefix_val[i + 1] = prefix_val[i]
                
        ans = []
        # Process each query in O(1) time
        for l, r in queries:
            # 1. Get the sum of digits in s[l..r]
            digit_sum = prefix_sum[r + 1] - prefix_sum[l]
            
            # 2. Get the number of non-zero digits in s[l..r]
            num_nonzero = prefix_nonzero[r + 1] - prefix_nonzero[l]
            
            # 3. Extract the integer value x mod MOD
            # x = (V[r] - V[l-1] * 10^(number of non-zeros in window)) % MOD
            x = (prefix_val[r + 1] - prefix_val[l] * pow10[num_nonzero]) % MOD
            
            # Calculate final answer for the query
            ans.append((x * digit_sum) % MOD)
            
        return ans