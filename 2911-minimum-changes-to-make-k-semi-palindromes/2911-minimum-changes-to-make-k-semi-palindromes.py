class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        
        # Precompute divisors for each length from 1 to n
        divisors = [[] for _ in range(n + 1)]
        for length in range(1, n + 1):
            for d in range(1, length):
                if length % d == 0:
                    divisors[length].append(d)
        
        # cost[i][j] stores the min changes to make s[i...j] a semi-palindrome
        cost = [[float('inf')] * n for _ in range(n)]
        
        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                min_c = float('inf')
                for d in divisors[length]:
                    current_cost = 0
                    # Check each of the d groups
                    for offset in range(d):
                        l = i + offset
                        r = j - d + 1 + offset
                        while l < r:
                            if s[l] != s[r]:
                                current_cost += 1
                            l += d
                            r -= d
                    min_c = min(min_c, current_cost)
                cost[i][j] = min_c
                
        # DP to partition into k substrings
        # dp[p][i] = min changes to partition s[0...i] into p parts
        dp = [[float('inf')] * n for _ in range(k + 1)]
        
        # Base case: 1 part from 0 to i
        for i in range(n):
            dp[1][i] = cost[0][i]
            
        for p in range(2, k + 1):
            for i in range(p - 1, n):
                for j in range(p - 2, i):
                    dp[p][i] = min(dp[p][i], dp[p - 1][j] + cost[j + 1][i])
                    
        return dp[k][n - 1]