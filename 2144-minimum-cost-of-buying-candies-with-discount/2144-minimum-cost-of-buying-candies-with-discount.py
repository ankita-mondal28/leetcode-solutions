class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        # Sort the costs in descending order so the most expensive ones are bought first
        cost.sort(reverse=True)
        
        total_cost = 0
        for i in range(len(cost)):
            # If the index is a multiple of 3 (0-indexed: 2, 5, 8...), 
            # this candy is free. Otherwise, we pay for it.
            if i % 3 != 2:
                total_cost += cost[i]
                
        return total_cost