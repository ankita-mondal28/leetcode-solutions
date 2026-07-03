from collections import deque

class Solution:
    def findMaxPathScore(self, edges: list[list[int]], online: list[bool], k: int) -> int:
        # Since 'n' isn't explicitly passed, calculate it from the length of online array
        n = len(online)
        
        # Step 1: Pre-filter edges to drop any connecting to offline intermediate nodes
        valid_edges = []
        max_edge_cost = -1
        
        for u, v, cost in edges:
            if online[u] and online[v]:
                valid_edges.append((u, v, cost))
                if cost > max_edge_cost:
                    max_edge_cost = cost
                    
        # If no valid edges exist at all, a path isn't possible
        if max_edge_cost == -1:
            return -1

        # Step 2: Build adjacency list and compute in-degrees for Topological Sort (DAG DP)
        adj = [[] for _ in range(n)]
        in_degree = [0] * n
        for u, v, cost in valid_edges:
            adj[u].append((v, cost))
            in_degree[v] += 1
            
        # Standard Kahn's algorithm to compute topological order
        topo_order = []
        queue = deque([i for i in range(n) if in_degree[i] == 0])
        while queue:
            node = queue.popleft()
            topo_order.append(node)
            for neighbor, _ in adj[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 3: Helper function to check if a valid path exists with minimum edge cost >= target_min
        def can_reach_with_min_cost(target_min: int) -> bool:
            # dp[i] stores the minimum total cost to reach node i from node 0
            dp = [float('inf')] * n
            dp[0] = 0
            
            for u in topo_order:
                if dp[u] == float('inf'):
                    continue
                for v, cost in adj[u]:
                    # Only cross the edge if it meets or exceeds our target threshold
                    if cost >= target_min:
                        if dp[u] + cost < dp[v]:
                            dp[v] = dp[u] + cost
                            
            return dp[n - 1] <= k

        # Step 4: Binary Search over the possible minimum edge costs
        low, high = 0, max_edge_cost
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            if can_reach_with_min_cost(mid):
                ans = mid       # Found a valid bottleneck threshold! Try to maximize it.
                low = mid + 1
            else:
                high = mid - 1  # Cannot complete path under this restriction, lower the threshold.
                
        return ans