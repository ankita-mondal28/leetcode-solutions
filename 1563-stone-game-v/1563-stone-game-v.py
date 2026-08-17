from functools import cache
from itertools import accumulate

class Solution:
    def stoneGameV(self, stoneValue: list[int]) -> int:
        n = len(stoneValue)
        # Prefix sum array to get range sums in O(1)
        prefix = [0] + list(accumulate(stoneValue))

        @cache
        def dfs(i: int, j: int) -> int:
            if i >= j:
                return 0

            max_score = 0
            total_sum = prefix[j + 1] - prefix[i]

            for k in range(i, j):
                l_sum = prefix[k + 1] - prefix[i]
                r_sum = total_sum - l_sum

                if l_sum < r_sum:
                    # Pruning: skip recursive call if it can't beat current max_score
                    if max_score < 2 * l_sum:
                        max_score = max(max_score, l_sum + dfs(i, k))
                elif l_sum > r_sum:
                    if max_score < 2 * r_sum:
                        max_score = max(max_score, r_sum + dfs(k + 1, j))
                    else:
                        # Since r_sum strictly decreases as k increases, 
                        # further iterations will never improve max_score
                        break
                else:
                    max_score = max(max_score, l_sum + max(dfs(i, k), dfs(k + 1, j)))

            return max_score

        return dfs(0, n - 1)