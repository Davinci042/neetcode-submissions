class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        seen = set()

        if not strs:
            return [[""]]
        if len(strs) == 1:
            return [[strs[0]]]
        
        for i, item in enumerate(strs):
            if i in seen:
                continue
            sublist = [item]
            seen.add(i)
            for j in range(i+1, len(strs)):
                if j not in seen and sorted(item) == sorted(strs[j]):
                    sublist.append(strs[j])
                    seen.add(j)

            result.append(list(sublist))

        return result
                        






                    

        