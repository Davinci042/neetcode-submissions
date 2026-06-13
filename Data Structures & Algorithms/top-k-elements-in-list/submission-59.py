class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        frequency = {}
        
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
                        
        result = sorted(frequency, key=frequency.get, reverse=True)[:k]

        return result



            




        