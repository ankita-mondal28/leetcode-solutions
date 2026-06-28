class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: list[int]) -> int:
        # Step 1: Sort the array
        arr.sort()
        
        # Step 2: The first element must start at 1
        current_max = 1
        
        # Step 3: Iterate through the rest of the elements
        for i in range(1, len(arr)):
            if arr[i] > current_max:
                current_max += 1
                
        # Step 4: Return the maximum possible value achieved
        return current_max