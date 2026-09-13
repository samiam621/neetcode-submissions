class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #hash map
        count={} #numbers : count 
        frequency=[[] for i in range(len(nums)+1)]
        
        #counting frequency of numbers 
        for n in nums:
           count[n] = 1 + count.get(n,0)
        #sorting numbers by acending frequency 1-k
        for n,c in count.items():
            frequency[c].append(n)

        results=[]

        # n:c
        # 1:1 2:2 3:3 #count
        #[[],[1],[2],[3],[],[],[]] #frequency
        #. 0, 1, 2, 3, 4, 5, 6 # index len 7

        #find the k most frequent elements in array
        for i in range(len(frequency)-1, 0,-1):
            for n in frequency[i]:
                if n in frequency[i]:
                    results.append(n)
                if len(results) == k:
                    return results
                
