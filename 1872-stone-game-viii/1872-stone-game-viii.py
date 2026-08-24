from typing import List

class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        
        # Step 1: Compute prefix sums in-place or via a new list
        prefix = [0] * n
        prefix[0] = stones[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + stones[i]
            
        # Step 2: Base case - at index n - 1, the player MUST take all stones
        # The score difference for taking prefix[n-1] with no remaining stones is prefix[n-1]
        dp = prefix[-1]
        
        # Step 3: Iterate backwards from n - 2 down to 1
        # Alice can pick any index x >= 1, so the final answer is dp evaluated at index 1.
        for i in range(n - 2, 0, -1):
            dp = max(dp, prefix[i] - dp)
            
        return dp