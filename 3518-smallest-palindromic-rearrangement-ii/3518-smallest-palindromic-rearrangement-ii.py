from collections import Counter
from math import comb

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        # Step 1: Count character frequencies for the left half
        full_counts = Counter(s)
        half_counts = [0] * 26
        mid_char = ""
        
        for char, count in full_counts.items():
            idx = ord(char) - ord('a')
            half_counts[idx] = count // 2
            if count % 2 == 1:
                mid_char = char

        # Helper to compute distinct permutations of remaining character counts
        def count_permutations(counts: list[int]) -> int:
            total_chars = sum(counts)
            res = 1
            for count in counts:
                if count > 0:
                    res *= comb(total_chars, count)
                    total_chars -= count
                    if res >= k:  # Cap at k to avoid huge numbers
                        return k
            return res

        # Step 2: Check if k is greater than total possible permutations
        total_perms = count_permutations(half_counts)
        if k > total_perms:
            return ""

        # Step 3: Build the left half character by character
        half_len = sum(half_counts)
        left_half = []

        for _ in range(half_len):
            for i in range(26):
                if half_counts[i] == 0:
                    continue
                
                # Try placing this character
                half_counts[i] -= 1
                perms = count_permutations(half_counts)
                
                if perms >= k:
                    left_half.append(chr(ord('a') + i))
                    break
                else:
                    k -= perms
                    half_counts[i] += 1  # Backtrack and try next character

        # Step 4: Reconstruct full palindrome
        left_str = "".join(left_half)
        return left_str + mid_char + left_str[::-1]