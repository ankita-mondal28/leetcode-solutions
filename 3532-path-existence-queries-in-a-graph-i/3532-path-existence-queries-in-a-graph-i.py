from typing import List

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        # component_id[i] will store the ID of the connected component node i belongs to
        component_id = [0] * n
        current_id = 0
        
        # Step 1: Group adjacent elements into components
        for i in range(1, n):
            # If the difference between consecutive values exceeds maxDiff,
            # they cannot be connected, so we start a new component group.
            if nums[i] - nums[i - 1] > maxDiff:
                current_id += 1
            component_id[i] = current_id
            
        # Step 2: Resolve each query in O(1) time
        ans = []
        for u, v in queries:
            # Nodes are reachable if and only if they share the same component group ID
            ans.append(component_id[u] == component_id[v])
            
        return ans