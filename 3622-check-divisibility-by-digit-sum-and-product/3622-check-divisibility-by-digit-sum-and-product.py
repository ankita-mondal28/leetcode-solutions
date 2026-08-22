class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digit_sum = 0
        digit_product = 1
        
        # Convert integer to string to process each digit
        for digit_char in str(n):
            digit = int(digit_char)
            digit_sum += digit
            digit_product *= digit
            
        total = digit_sum + digit_product
        
        # Check if n is divisible by the combined total
        return n % total == 0