class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for v in s:
            val = 0
            if v == "(":    
                stack.append(0)
            else:                
                while stack[-1] != 0:
                    val += stack.pop()
                val = max(2*val , 1)
                stack.pop()
                stack.append(val)
        return sum(stack)