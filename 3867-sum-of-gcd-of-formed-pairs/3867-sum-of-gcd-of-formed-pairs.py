import math

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefixGcd = []
        max_val = 0
        
        for num in nums:
            if num > max_val:
                max_val = num
            prefixGcd.append(math.gcd(num, max_val))
            
        prefixGcd.sort()
        
        total_sum = 0
        left, right = 0, len(prefixGcd) - 1
        
        while left < right:
            total_sum += math.gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1
            
        return total_sum