class Solution:
    def reverseSubmatrix(self, grid: list[list[int]], x: int, y: int, k: int) -> list[list[int]]:
        # Swap rows from top to middle
        for i in range(k // 2):
            top_row = x + i
            bottom_row = x + k - 1 - i
            
            # Swap elements in columns belonging to the submatrix
            for j in range(y, y + k):
                grid[top_row][j], grid[bottom_row][j] = grid[bottom_row][j], grid[top_row][j]
                
        return grid