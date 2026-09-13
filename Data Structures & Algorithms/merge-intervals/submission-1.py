class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sort by start val
        intervals.sort(key=lambda x: x[0])
        results=[intervals[0]]

        #if end of prev sub array is greater than or equal to the start of  
        #curr sub array
        #then overlap: new sub array [prev start, curr end]
        
        for start,end in intervals[1:]:
            #overlap check
            prevEnd = results[-1][1]
            if prevEnd >= start:
                results[-1][1] = max(prevEnd, end)
            else:
                results.append([start,end])
        
        return results