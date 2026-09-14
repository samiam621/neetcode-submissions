class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        chars = {} #sorted_word: word
        for word in strs:
            sorted_word="".join(sorted(word))
            if sorted_word not in chars:
                chars[sorted_word]= []
            chars[sorted_word].append(word)

        return list(chars.values())
            