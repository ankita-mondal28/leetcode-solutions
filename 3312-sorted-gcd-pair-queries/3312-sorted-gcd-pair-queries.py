import bisect
from typing import List

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_val = max(nums)
        
        # Count frequency of each number in nums
        freq = [0] * (max_val + 1)
        for num in nums:
            freq[num] += 1
            
        # gcd_count[x] will store the exact number of pairs with GCD equal to x
        gcd_count = [0] * (max_val + 1)
        
        # Iterate backwards to use inclusion-exclusion
        for x in range(max_val, 0, -1):
            # Count how many numbers in nums are multiples of x
            multiples_count = 0
            for y in range(x, max_val + 1, x):
                multiples_count += freq[y]
                
            # Total pairs that have a common divisor x (GCD is a multiple of x)
            total_pairs = multiples_count * (multiples_count - 1) // 2
            
            # Subtract pairs where the actual GCD is a strictly larger multiple of x
            for y in range(2 * x, max_val + 1, x):
                total_pairs -= gcd_count[y]
                
            gcd_count[x] = total_pairs
            
        # Build prefix sums of the number of pairs to enable binary search
        prefix_sums = []
        current_sum = 0
        valid_gcds = []
        
        for x in range(1, max_val + 1):
            if gcd_count[x] > 0:
                current_sum += gcd_count[x]
                prefix_sums.append(current_sum)
                valid_gcds.append(x)
                
        # Answer each query using binary search
        ans = []
        for q in queries:
            idx = bisect.bisect_right(prefix_sums, q)
            ans.append(valid_gcds[idx])
            
        return ans