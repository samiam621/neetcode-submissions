class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #while new area is less than previous area
        #slide r; get the width = j-i; get the min height and then calculate new  area; then compare the new area with the old area and area = max(new,old)
        # 
        #then area is abs(index1 - index 2) * height
        
        l,r = 0, len(heights)-1
        width, height = 0,0

        area = 0
    
        while l < r:
            width = abs(r-l)
            height = min(heights[l],heights[r])
            area = max(area,width * height)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -=1

        return area