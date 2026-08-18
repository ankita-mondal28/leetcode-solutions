class Solution:
    def maxProductPath(self, grid: list[list[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        max_dp = [[0] * n for _ in range(m)]
        min_dp = [[0] * n for _ in range(m)]
        
        # Base case initialization
        max_dp[0][0] = min_dp[0][0] = grid[0][0]
        
        # Initialize first row (can only arrive from left)
        for j in range(1, n):
            max_dp[0][j] = min_dp[0][j] = max_dp[0][j - 1] * grid[0][j]
            
        # Initialize first column (can only arrive from top)
        for i in range(1, m):
            max_dp[i][0] = min_dp[i][0] = max_dp[i - 1][0] * grid[i][0]
            
        # Fill DP tables
        for i in range(1, m):
            for j in range(1, n):
                val = grid[i][j]
                if val >= 0:
                    max_dp[i][j] = max(max_dp[i - 1][j], max_dp[i][j - 1]) * val
                    min_dp[i][j] = min(min_dp[i - 1][j], min_dp[i][j - 1]) * val
                else:
                    max_dp[i][j] = min(min_dp[i - 1][j], min_dp[i][j - 1]) * val
                    min_dp[i][j] = max(max_dp[i - 1][j], max_dp[i][j - 1]) * val
                    
        res = max_dp[m - 1][n - 1]
        return res % MOD if res >= 0 else -1