class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr=set() #char 
        l=0
        result=0
        
        for r in range(len(s)):
            while s[r] in substr:
                substr.remove(s[l])
                l+=1
            substr.add(s[r])
            result = max(result, r-l+1)
        return result