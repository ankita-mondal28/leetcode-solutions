class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 1)  # dp[i] = max advantage for player starting at index i
        
        for i in range(n - 1, -1, -1):
            take_sum = 0
            best_diff = float('-inf')
            
            # A player can pick 1, 2, or 3 stones
            for x in range(1, 4):
                if i + x <= n:
                    take_sum += stoneValue[i + x - 1]
                    # Subtract dp[i + x] because it represents the opponent's relative score
                    best_diff = max(best_diff, take_sum - dp[i + x])
                    
            dp[i] = best_diff
            
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"