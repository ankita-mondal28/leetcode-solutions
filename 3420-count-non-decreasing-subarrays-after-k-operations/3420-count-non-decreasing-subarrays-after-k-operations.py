import collections

class Solution:
    def countNonDecreasingSubarrays(self, nums: list[int], k: int) -> int:
        ans = 0
        cost = 0
        # Store indices of nums such that the corresponding values form a monotonic structure.
        dq = collections.deque()
        j = len(nums) - 1
        
        # Traverse from right to left
        for i, num in reversed(list(enumerate(nums))):
            while dq and nums[dq[-1]] < num:
                l = dq.pop()
                r = dq[-1] if dq else j + 1
                cost += (r - l) * (num - nums[l])
            
            dq.append(i)
            
            # Shrink the window from the right if the cost exceeds k
            while cost > k:
                cost -= nums[dq[0]] - nums[j]
                if dq[0] == j:
                    dq.popleft()
                j -= 1
                
            ans += j - i + 1
            
        return ans