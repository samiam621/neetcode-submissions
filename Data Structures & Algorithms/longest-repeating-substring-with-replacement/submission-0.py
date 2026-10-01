class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} #letter : count
        res = 0

        #valid if current window - count of most frequent char <= k
        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            
            #while window is invalid
            while (r-l+1) - max(count.values()) > k:  
                count[s[l]] -= 1
                l += 1
                
            #while its valid
            res = max(res, r-l+1)
        return res


        