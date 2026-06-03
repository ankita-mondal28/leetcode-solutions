from typing import List

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total = 0
        neg = 0
        mn = float('inf')

        for row in matrix:
            for x in row:
                if x < 0:
                    neg += 1
                    x = -x

                total += x

                if x < mn:
                    mn = x

        return total if (neg & 1) == 0 else total - (mn << 1)