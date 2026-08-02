class Solution:
    def stoneGame(self, piles: list[int]) -> bool:
        n = len(piles)
        # dp[i] stores the max score advantage for the current subsegment starting at index i
        dp = piles.copy()
        
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i] = max(piles[i] - dp[i + 1], piles[j] - dp[i])
                
        return dp[0] > 0