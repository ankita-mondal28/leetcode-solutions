from collections import defaultdict, deque

class Solution:
    def minScore(self, n: int, roads: list[list[int]]) -> int:
        # Step 1: Build the adjacency list
        # graph[u] = [(v, distance), ...]
        graph = defaultdict(list)
        for u, v, dist in roads:
            graph[u].append((v, dist))
            graph[v].append((u, dist))
            
        # Step 2: BFS to traverse the connected component starting at city 1
        min_score = float('inf')
        visited = set()
        queue = deque([1])
        visited.add(1)
        
        while queue:
            node = queue.popleft()
            
            # Explore all neighbors of the current city
            for neighbor, dist in graph[node]:
                # Update the minimum score seen so far for ANY edge in this component
                min_score = min(min_score, dist)
                
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
        return min_score