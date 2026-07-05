class Solution:
    def pathsWithMaxScore(self, board: list[str]) -> list[int]:
        n = len(board)
        MOD = 10**9 + 7
        
        # max_score[r][c] will store the maximum sum to reach (r, c)
        # Initialize with -1 to indicate unreachability
        max_score = [[-1] * n for _ in range(n)]
        
        # path_count[r][c] will store the number of paths achieving that maximum sum
        path_count = [[0] * n for _ in range(n)]
        
        # Base case: Starting point 'S' at the bottom-right corner
        max_score[n - 1][n - 1] = 0
        path_count[n - 1][n - 1] = 1
        
        # Fill the DP table from bottom to top, right to left
        for r in range(n - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                # Skip obstacles and the starting cell itself
                if board[r][c] == 'X' or (r == n - 1 and c == n - 1):
                    continue
                
                # Check three possible incoming transitions
                # (down, right, down-right)
                directions = [(r + 1, c), (r, c + 1), (r + 1, c + 1)]
                best_score = -1
                ways = 0
                
                for nr, nc in directions:
                    if nr < n and nc < n and max_score[nr][nc] != -1:
                        if max_score[nr][nc] > best_score:
                            best_score = max_score[nr][nc]
                            ways = path_count[nr][nc]
                        elif max_score[nr][nc] == best_score:
                            ways = (ways + path_count[nr][nc]) % MOD
                
                # If at least one valid incoming path was found
                if best_score != -1:
                    # Calculate the current cell's value
                    current_val = 0
                    if board[r][c].isdigit():
                        current_val = int(board[r][c])
                    
                    max_score[r][c] = best_score + current_val
                    path_count[r][c] = ways
                    
        # If the destination 'E' at (0, 0) is unreachable, return [0, 0]
        if max_score[0][0] == -1:
            return [0, 0]
            
        return [max_score[0][0], path_count[0][0]]