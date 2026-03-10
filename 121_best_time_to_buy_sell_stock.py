class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_p = prices[0]
        best = 0
        for p in prices:
            if p < min_p:
                min_p = p
            elif p - min_p > best:
                best = p - min_p
        return best