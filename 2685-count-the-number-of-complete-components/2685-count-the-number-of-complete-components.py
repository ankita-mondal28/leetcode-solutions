from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # Step 1: Build the adjacency list representation
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        visited = [False] * n
        complete_components_count = 0
        
        # Step 2: Explore each connected component
        for i in range(n):
            if not visited[i]:
                # Track vertices and total edge counts for the current component
                vertex_count = 0
                edge_count = 0
                
                # Iterative DFS using a stack
                stack = [i]
                visited[i] = True
                
                while stack:
                    curr = stack.pop()
                    vertex_count += 1
                    edge_count += len(adj[curr])
                    
                    for neighbor in adj[curr]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            stack.append(neighbor)
                
                # Step 3: Check if the component is complete
                # Since each undirected edge is counted twice (once from each endpoint),
                # the total degree sum (edge_count) must equal vertex_count * (vertex_count - 1).
                if edge_count == vertex_count * (vertex_count - 1):
                    complete_components_count += 1
                    
        return complete_components_count