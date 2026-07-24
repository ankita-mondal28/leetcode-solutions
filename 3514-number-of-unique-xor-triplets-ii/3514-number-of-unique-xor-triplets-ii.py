from typing import List

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        unique_nums = list(set(nums))
        
        # Step 1: Find all possible pair XORs (a ^ b)
        pair_xors = set()
        n = len(unique_nums)
        for i in range(n):
            for j in range(i, n):
                pair_xors.add(unique_nums[i] ^ unique_nums[j])
                
        # Step 2: Combine pair XORs with a 3rd element (a ^ b ^ c)
        triplet_xors = set()
        for p in pair_xors:
            for c in unique_nums:
                triplet_xors.add(p ^ c)
                
        return len(triplet_xors)