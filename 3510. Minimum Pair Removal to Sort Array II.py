import heapq

class Solution:
    def minimumPairRemoval(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        
        vals = list(nums)
        nexts = [i + 1 for i in range(n)]
        prevs = [i - 1 for i in range(n)]
        nexts[-1] = -1
        
        removed = [False] * n
        version = [0] * n 
        
        pq = []
        unsorted_cnt = 0
        
        for i in range(n - 1):
            if vals[i] > vals[i + 1]:
                unsorted_cnt += 1
            pq.append((vals[i] + vals[i + 1], i, 0))
            
        heapq.heapify(pq)
            
        if unsorted_cnt == 0:
            return 0
            
        moves = 0
        
        while unsorted_cnt > 0 and pq:
            pair_sum, u, v_id = heapq.heappop(pq)
            
            if removed[u] or version[u] != v_id:
                continue
            v = nexts[u]
            if v == -1 or removed[v]:
                continue
                
            moves += 1
            
            if vals[u] > vals[v]:
                unsorted_cnt -= 1
                
            p = prevs[u]
            if p != -1 and vals[p] > vals[u]:
                unsorted_cnt -= 1
                
            nxt_v = nexts[v]
            if nxt_v != -1 and vals[v] > vals[nxt_v]:
                unsorted_cnt -= 1
                
            vals[u] = pair_sum
            removed[v] = True
            
            nexts[u] = nxt_v
            if nxt_v != -1:
                prevs[nxt_v] = u
                
            if p != -1 and vals[p] > vals[u]:
                unsorted_cnt += 1
            if nxt_v != -1 and vals[u] > vals[nxt_v]:
                unsorted_cnt += 1
                
            version[u] += 1
            if nxt_v != -1:
                heapq.heappush(pq, (vals[u] + vals[nxt_v], u, version[u]))
                
            if p != -1:
                version[p] += 1
                heapq.heappush(pq, (vals[p] + vals[u], p, version[p]))
                
        return moves