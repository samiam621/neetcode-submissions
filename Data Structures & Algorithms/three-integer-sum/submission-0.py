class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort the array
        #plan: use two pointer r, l for start and end, and have
        # i check duplicates  using a hashmap
        #no duplicates so if num in seen={}
        #if l > 0 (left becomes positive, no way to get 0) so end
        nums.sort()
        results =[]

        for i in range(len(nums)):
            l,r=i+1,len(nums)-1
            #check duplicate or if i is positive
            if i > 0 and nums[i-1] == nums[i]:
                continue  
            
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
            
