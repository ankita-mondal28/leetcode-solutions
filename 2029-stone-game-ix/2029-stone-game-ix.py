class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        cnt = [0, 0, 0]
        for stone in stones:
            cnt[stone % 3] += 1
            
        cnt0, cnt1, cnt2 = cnt[0], cnt[1], cnt[2]
        
        # If count of 0-remainder stones is even
        if cnt0 % 2 == 0:
            return cnt1 >= 1 and cnt2 >= 1
            
        # If count of 0-remainder stones is odd
        return abs(cnt1 - cnt2) > 2