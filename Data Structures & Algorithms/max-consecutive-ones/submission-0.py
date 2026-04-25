class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counts = []
        current_max = 0
        count = 0
         
        for num in nums:
            if num == 1:
                count +=1
            else:
                counts.append(count)
                count = 0
        counts.append(count)

        for count in counts:
            if count > current_max:
                current_max = count
                
        return current_max
