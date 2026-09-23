class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1
        return min(nums)
        while l < r:
            mid = (l+r) // 2
            #ex [4,5,6,7,0,1,2]
            if nums[mid] >= nums[l]:
                #search right
                #l becomes mid + 1
                l = mid + 1

            else:
                #search left
                #r becomes mid -1
                r = mid -1
        
        return