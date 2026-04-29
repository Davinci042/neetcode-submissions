class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ops = []

        for op in operations:
                if op == "+":
                    result = ops[-1] + ops[-2]
                    ops.append(result)
                        
                elif op == 'C':
                    ops.pop()

                elif op == 'D':
                    value = int(ops[-1])
                    ops.append(value * 2)
            
                else:
                    ops.append(int(op))
        
        return sum(ops)


        