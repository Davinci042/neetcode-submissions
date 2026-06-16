import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''prefix = [nums[0]]

        for i in range(1, len(nums)):
            prefix.append(prefix[-1] * nums[i])

        return prefix'''

        result = []

        for i, item in enumerate(nums):
            sublist = [item for j, item in enumerate(nums) if j != i]
            if len(sublist) == 1:
                value = sublist[0]
                result.append(value)
            else:
                value = math.prod(sublist)
                result.append(value)
        
        return result
