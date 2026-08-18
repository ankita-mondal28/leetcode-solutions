from collections import Counter

class Solution:
    def largestInteger(self, nums: list[int], k: int) -> int:
        n = len(nums)
        
        # Case 1: k equals the length of the array
        if k == n:
            return max(nums)
        
        counts = Counter(nums)
        
        # Case 2: k is 1
        if k == 1:
            valid = [x for x in nums if counts[x] == 1]
            return max(valid) if valid else -1
            
        # Case 3: 1 < k < n
        ans = -1
        # Check first element: valid if unique in nums
        if counts[nums[0]] == 1:
            ans = max(ans, nums[0])
            
        # Check last element: valid if unique in nums
        if counts[nums[-1]] == 1:
            ans = max(ans, nums[-1])
            
        return ans