from heapq import heappush, heappop

class Solution:
    def maxTotalValue(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if n == 0:
            return 0
            
        max_log = n.bit_length()
        
        lg = [0] * (n + 1)
        for i in range(2, n + 1):
            lg[i] = lg[i >> 1] + 1
            
        f_max = [[0] * max_log for _ in range(n)]
        f_min = [[0] * max_log for _ in range(n)]
        
        for i in range(n):
            f_max[i][0] = nums[i]
            f_min[i][0] = nums[i]
            
        for j in range(1, max_log):
            length = 1 << (j - 1)
            for i in range(n - (1 << j) + 1):
                f_max[i][j] = max(f_max[i][j - 1], f_max[i + length][j - 1])
                f_min[i][j] = min(f_min[i][j - 1], f_min[i + length][j - 1])
                
        def query_val(l: int, r: int) -> int:
            k_log = lg[r - l + 1]
            shift = r - (1 << k_log) + 1
            mx = max(f_max[l][k_log], f_max[shift][k_log])
            mn = min(f_min[l][k_log], f_min[shift][k_log])
            return mx - mn

        pq = []
        for l in range(n):
            heappush(pq, (-query_val(l, n - 1), l, n - 1))
            
        total_value = 0
        
        push, pop = heappush, heappop
        
        for _ in range(k):
            neg_val, l, r = pop(pq)
            total_value -= neg_val
            
            if r > l:
                next_r = r - 1
                push(pq, (-query_val(l, next_r), l, next_r))
                
        return total_value