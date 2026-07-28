class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        
        # Take the first half of the string
        half_length = n // 2
        first_half = sorted(s[:half_length])
        
        left = "".join(first_half)
        right = left[::-1]  # Mirror of the left half
        
        # If length is odd, keep the middle character in place
        mid = s[half_length] if n % 2 == 1 else ""
        
        return left + mid + right