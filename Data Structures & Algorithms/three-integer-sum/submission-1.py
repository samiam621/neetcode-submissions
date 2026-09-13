class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort the array
        #plan: use two pointer r, l for i+1 and end, and have
        # i check duplicates  using a set
        #once i+r+l nums == 0, move left to non duplicate and less than r
    
        nums.sort()
        results =[]
        seen = set()

        for i in range(len(nums)):
            l,r=i+1,len(nums)-1
            #check duplicate or if i is positive
            if nums[i] in seen:
                continue  
            seen.add(nums[i])
            
            while l < r:
                threeSum = nums[l] + nums[r] + nums[i]
                if threeSum == 0:
                    results.append([nums[i],nums[l],nums[r]])
                    #next num
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    l += 1

        return results
            
