class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: If there's only 1 row, or the string is shorter than rows,
        # the zigzag pattern is just the string itself.
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Initialize rows as an array of strings
        rows = ["" for _ in range(numRows)]
        
        current_row = 0
        direction = -1  # Negative initially so the first step flips it to 1 (down)
        
        for char in s:
            rows[current_row] += char
            
            # If we are at the top row or bottom row, reverse the direction
            if current_row == 0 or current_row == numRows - 1:
                direction = -direction
                
            current_row += direction
            
        # Combine all rows together to form the final string
        return "".join(rows)