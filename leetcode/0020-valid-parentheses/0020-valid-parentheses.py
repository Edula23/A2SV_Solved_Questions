class Solution:
    def isValid(self, s: str) -> bool:
        values = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for c in s:
            if c in values:  
                stack.append(c)
            else:  
                if not stack or values[stack.pop()] != c:
                    return False
        return not stack
                