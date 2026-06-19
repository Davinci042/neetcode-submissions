class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
         l_arr = [0] * len(nums)
         r_arr = [0] * len(nums)
         prefix = 1
         postfix = 1

         for i in range(len(nums)):
            j = -i - 1
            l_arr[i] = prefix
            r_arr[j] = postfix
            prefix *= nums[i]
            postfix *= nums[j]

         return [l * r for l, r in zip(l_arr, r_arr)]

        
        