class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    
        cache={}
        return self.dp(text1,text2,0,0,cache)    


    def dp(self,text1,text2,i,j,cache) -> int:
        #base case
        if i not in range(len(text1))or j not in range(len(text2)):
            return 0
        #check cache
        if (i,j) in cache:
            return cache[(i,j)]
        #recursion
        if text1[i] == text2[j]:
            result1 = 1 + self.dp(text1,text2,i+1,j+1,cache)
            cache[(i,j)] = result1
            return result1
        elif text1[i] != text2[j]:
            if (i,j) not in cache:
                result2 = max(self.dp(text1,text2,i+1,j,cache),self.dp(text1,text2,i,j+1,cache))  
                cache[(i,j)] = result2
            return result2


        
