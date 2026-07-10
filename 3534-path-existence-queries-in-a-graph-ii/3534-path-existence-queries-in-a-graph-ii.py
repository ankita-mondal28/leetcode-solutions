from typing import List

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        # Step 1: Pair values with their original indices and sort them
        sorted_nodes = sorted((nums[i], i) for i in range(n))
        
        # Map original index -> its position in the sorted array
        pos = [0] * n
        for sorted_idx, (val, orig_idx) in enumerate(sorted_nodes):
            pos[orig_idx] = sorted_idx
            
        # Step 2: Compute the farthest right index reachable in 1 hop using two pointers
        next_hop = [0] * n
        right = 0
        for left in range(n):
            while right < n and sorted_nodes[right][0] - sorted_nodes[left][0] <= maxDiff:
                right += 1
            next_hop[left] = right - 1  # Farthest index within maxDiff

        # Step 3: Build the Binary Lifting Table
        LOG = 18  # 2^17 = 131,072 > 10^5 nodes
        st = [[0] * LOG for _ in range(n)]
        
        for i in range(n):
            st[i][0] = next_hop[i]
            
        for j in range(1, LOG):
            for i in range(n):
                st[i][j] = st[st[i][j - 1]][j - 1]
                
        # Step 4: Process each query using binary lifting
        ans = []
        for u, v in queries:
            if u == v:
                ans.append(0)
                continue
                
            # Get sorted positions
            a, b = pos[u], pos[v]
            if a > b:
                a, b = b, a  # Enforce left-to-right processing
                
            curr = a
            steps = 0
            
            # Greedily jump as far right as possible staying strictly before b
            for j in range(LOG - 1, -1, -1):
                if st[curr][j] < b:
                    curr = st[curr][j]
                    steps += (1 << j)
                    
            # Check if one final hop can cover or pass b
            if st[curr][0] >= b:
                ans.append(steps + 1)
            else:
                ans.append(-1)  # Target is unreachable
                
        return ans