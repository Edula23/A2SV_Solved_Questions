class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        op = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y
        }
        
        def rec(l, r):
            res = []
            for i in range(l, r+1):
                if expression[i] in op:
                    n1 = rec(l, i-1)
                    n2 = rec(i+1, r)

                    for a in n1:
                        for b in n2:
                            res.append(op[expression[i]](a, b))
            if res == []:
                res.append(int(expression[l:r+1]))
            return res
        return rec(0, len(expression)-1)





            
