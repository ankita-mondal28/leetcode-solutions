class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        nums.sort()
        
        # Option 1: Product of three largest numbers
        option1 = nums[-1] * nums[-2] * nums[-3]
        
        # Option 2: Product of two smallest (negative) numbers and largest number
        option2 = nums[0] * nums[1] * nums[-1]
        
        return max(option1, option2)