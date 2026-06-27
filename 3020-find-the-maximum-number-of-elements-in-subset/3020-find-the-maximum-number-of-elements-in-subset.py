from collections import Counter

class Solution:
    def maximumLength(self, nums: list[int]) -> int:
        count = Counter(nums)
        max_len = 0
        
        # Handle the edge case for 1s
        if 1 in count:
            c = count[1]
            max_len = c if c % 2 != 0 else c - 1
            
        # Check for all other bases > 1
        for x in count:
            if x == 1:
                continue
                
            current_len = 0
            current_base = x
            
            # Keep squaring while we have at least 2 elements to flank the sides
            while current_base in count and count[current_base] >= 2:
                current_len += 2
                current_base = current_base * current_base
            
            # The loop stopped either because current_base has 1 element (perfect peak)
            # or it has 0 elements (we over-extended and the previous element must be the peak)
            if current_base in count and count[current_base] >= 1:
                current_len += 1
            else:
                # If the next square doesn't exist, the last element we processed
                # must act as the single peak instead of a pair.
                current_len -= 1 
                
            max_len = max(max_len, current_len)
            
        return max_len