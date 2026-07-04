class Solution:
    def myAtoi(self, s: str) -> int:
        # Define 32-bit signed integer boundaries
        INT_MIN = -2147483648
        INT_MAX = 2147483647
        
        n = len(s)
        i = 0
        
        # Step 1: Skip leading whitespaces
        while i < n and s[i] == ' ':
            i += 1
            
        # If we reached the end of the string, return 0
        if i == n:
            return 0
            
        # Step 2: Check for sign
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
            
        # Step 3: Read digits and construct the integer
        result = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            result = result * 10 + digit
            i += 1
            
        # Apply the sign
        result *= sign
        
        # Step 4: Handle clamping / overflow boundaries
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
            
        return result