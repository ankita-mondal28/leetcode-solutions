class Solution:
    def removeCoveredIntervals(self, intervals: list[list[int]]) -> int:
        # Sort by start point ascending, and by end point descending
        intervals.sort(key=lambda x: (x[0], -x[1]))
        
        remaining_count = 0
        max_end = 0
        
        for start, end in intervals:
            # If the current end extends beyond the maximum end seen so far,
            # this interval is NOT covered.
            if end > max_end:
                remaining_count += 1
                max_end = end  # Update the boundaries of the covering interval
                
        return remaining_count