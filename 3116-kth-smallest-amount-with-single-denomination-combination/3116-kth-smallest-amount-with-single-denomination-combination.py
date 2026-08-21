import math

class Solution:
    def findKthSmallest(self, coins: list[int], k: int) -> int:
        n = len(coins)
        
        # Precompute (lcm, sign) for all 2^N - 1 non-empty subsets
        subsets = []
        for mask in range(1, 1 << n):
            current_lcm = 1
            bits_count = 0
            for i in range(n):
                if (mask >> i) & 1:
                    bits_count += 1
                    current_lcm = math.lcm(current_lcm, coins[i])
            
            # Odd size subsets add (+1), even size subsets subtract (-1)
            sign = 1 if bits_count % 2 == 1 else -1
            subsets.append((current_lcm, sign))

        # Count unique multiples of any coin <= target using Inclusion-Exclusion
        def count_amounts(target: int) -> int:
            return sum(sign * (target // lcm_val) for lcm_val, sign in subsets)

        # Binary Search on the answer
        low = 1
        high = min(coins) * k
        ans = high

        while low <= high:
            mid = (low + high) // 2
            if count_amounts(mid) >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans