class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        chars= defaultdict(list)
        for word in strs:
            sorted_word="".join(sorted(word))
            chars[sorted_word].append(word)

        return list(chars.values())
            