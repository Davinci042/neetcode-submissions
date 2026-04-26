class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums
        i = 0

        for i in range(len(nums)):
            num = nums[i]
            ans.append(num)

        return ans
        