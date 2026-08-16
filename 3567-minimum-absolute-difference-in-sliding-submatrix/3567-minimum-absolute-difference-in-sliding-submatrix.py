from itertools import pairwise

class Solution:
    def minAbsDiff(self, grid: list[list[int]], k: int) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]
        
        for i in range(m - k + 1):
            for j in range(n - k + 1):
                # Extract all elements from the k x k submatrix
                nums = [grid[x][y] for x in range(i, i + k) for y in range(j, j + k)]
                nums.sort()
                
                # Check adjacent distinct pairs
                min_diff = min((b - a for a, b in pairwise(nums) if a != b), default=0)
                ans[i][j] = min_diff
                
        return ans