class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # Track the last seen index of 'a', 'b', and 'c'
        # Initialize with -1 to represent that they haven't been seen yet
        last_seen = {'a': -1, 'b': -1, 'c': -1}
        count = 0
        
        for right in range(len(s)):
            # Update the last seen index of the current character
            last_seen[s[right]] = right
            
            # If all three characters have been seen at least once
            if last_seen['a'] != -1 and last_seen['b'] != -1 and last_seen['c'] != -1:
                # The earliest index among the three characters defines our valid window start
                min_idx = min(last_seen['a'], last_seen['b'], last_seen['c'])
                
                # All prefixes from index 0 up to min_idx can form a valid substring ending at 'right'
                count += min_idx + 1
                
        return count