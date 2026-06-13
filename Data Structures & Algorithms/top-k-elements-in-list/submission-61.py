class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
                        
        return sorted(frequency, key=frequency.get, reverse=True)[:k]

    



            




        