from collections import deque

class Solution:
    def findSafeWalk(self, grid: list[list[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        
        # dist[i][j] stores the minimum health points lost to reach cell (i, j)
        dist = [[float('inf')] * n for _ in range(m)]
        
        # Initialize starting point
        dist[0][0] = grid[0][0]
        queue = deque([(0, 0)])
        
        # 4-directional movement vectors
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            r, c = queue.popleft()
            
            # If we reached the bottom-right corner, we can prematurely check, 
            # but since 0-1 BFS guarantees optimal path structure, finishing the BFS works perfectly.
            if r == m - 1 and c == n - 1:
                continue
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check grid boundaries
                if 0 <= nr < m and 0 <= nc < n:
                    weight = grid[nr][nc]
                    
                    # If a strictly less damaging path to (nr, nc) is discovered
                    if dist[r][c] + weight < dist[nr][nc]:
                        dist[nr][nc] = dist[r][c] + weight
                        
                        # 0-1 BFS core sorting logic
                        if weight == 0:
                            queue.appendleft((nr, nc))
                        else:
                            queue.append((nr, nc))
                            
        # Check if the final remaining health is at least 1
        return health - dist[m - 1][n - 1] >= 1