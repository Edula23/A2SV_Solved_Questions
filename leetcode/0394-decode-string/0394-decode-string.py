class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c != "]":
                stack.append(c)
            else:
                temp = ""
                while stack[-1] != "[":
                    temp = stack[-1] + temp
                    stack.pop()
                stack.pop()
                c = ""
                print(stack)
                while stack and stack[-1].isdigit():
                    c = stack[-1] + c
                    stack.pop()
                stack.append(int(c) * temp)
        return "".join(stack)









