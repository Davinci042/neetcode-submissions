class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        p = 0
        r = p + 1
        result = []

        while p < len(arr)-1:
            tmp = arr[r:]
            i = 0
            max_value = tmp[i]
            for i in range (1, len(tmp)):
                if tmp[i] > max_value:
                    max_value = tmp[i]
            result.append(max_value)
            arr.pop(0)
        result.append(-1)

        return result


        