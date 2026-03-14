class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        stack = []
        for log in logs:
            if stack and log == "../" :
                stack.pop()
            elif log == "./":
                continue
            elif log != "../":
                print(log)
                stack.append(log)
        return len(stack)
