class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        ans = 0
        i = 0
        n = len(s)
        pre = float('-inf')
        mx = 0
        
        while i < n:
            j = i + 1
            while j < n and s[j] == s[i]:
                j += 1
            
            cur = j - i
            if s[i] == '1':
                ans += cur
            else:
                mx = max(mx, pre + cur)
                pre = cur
            
            i = j
            
        return ans + mx