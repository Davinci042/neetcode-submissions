class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ops = []
        score = 0

        for op in operations:
                if op == "+":
                    result = ops[-1] + ops[-2]
                    ops.append(int(result))
                        
                elif op == 'C':
                    ops.pop()

                elif op == 'D':
                    value = int(ops[-1])
                    ops.append(value * 2)
            
                else:
                    ops.append(int(op))
        

        for x in ops:
            score += int(x)

        return score


        