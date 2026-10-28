class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # dp[j] will store the set of possible XOR values for the current row at column j
        dp = [set() for _ in range(n)]
        
        # Base case: top-left cell
        dp[0].add(grid[0][0])
        
        # Fill first row
        for j in range(1, n):
            for val in dp[j-1]:
                dp[j].add(val ^ grid[0][j])
                
        # Fill the rest of the grid
        for i in range(1, m):
            new_dp = [set() for _ in range(n)]
            
            # First column of current row only comes from above
            for val in dp[0]:
                new_dp[0].add(val ^ grid[i][0])
                
            for j in range(1, n):
                # Come from left
                for val in new_dp[j-1]:
                    new_dp[j].add(val ^ grid[i][j])
                # Come from above
                for val in dp[j]:
                    new_dp[j].add(val ^ grid[i][j])
                    
            dp = new_dp
            
        # The answer is the minimum value in the bottom-right cell's set
        return min(dp[n-1])