class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        total_xor = 0
        has_non_zero = False
        
        for num in nums:
            total_xor ^= num
            if num != 0:
                has_non_zero = True
                
        if total_xor != 0:
            return n
        
        if has_non_zero:
            return n - 1
        
        return 0