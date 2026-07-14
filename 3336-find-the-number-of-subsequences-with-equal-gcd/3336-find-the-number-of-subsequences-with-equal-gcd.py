import math
from functools import cache
from typing import List

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 1_000_000_007
        
        @cache
        def dp(i: int, x: int, y: int) -> int:
            if i == len(nums):
                return int(x > 0 and x == y)
            
            res = dp(i + 1, x, y)
            res = (res + dp(i + 1, math.gcd(x, nums[i]), y)) % MOD
            res = (res + dp(i + 1, x, math.gcd(y, nums[i]))) % MOD
            
            return res
            
        return dp(0, 0, 0)