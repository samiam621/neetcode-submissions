class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        chars = {} #sorted_word: word
        results=[]
        for word in strs:
            sorted_word="".join(sorted(word))
            if sorted_word not in chars:
                chars[sorted_word]= []
            chars[sorted_word].append(word)
        
        for word in chars.values():
            results.append(word)
        return results
            