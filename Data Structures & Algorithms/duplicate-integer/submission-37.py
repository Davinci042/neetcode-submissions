class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = False
        j = 0
 
        for j in range (len(nums)-1):
            k = j + 1
            while k <= len(nums)-1:
                if nums[j] == nums[k]:
                    result = True
                    break
                else:
                    k += 1
        return result
            

            
        
        