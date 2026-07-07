class Solution:
    def sumAndMultiply(self, n: int) -> int:
        # Step 1: Extract non-zero digit strings
        digits = [ch for ch in str(n) if ch != '0']
        
        # Edge case: If there are no non-zero digits
        if not digits:
            return 0
        
        # Step 2: Form the new integer x
        x = int("".join(digits))
        
        # Step 3: Compute the sum of the digits in x
        digit_sum = sum(int(ch) for ch in digits)
        
        # Step 4: Return x multiplied by sum
        return x * digit_sum