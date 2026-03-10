class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        ans = []
        for char in path:
            if char == '.':
                continue
            elif char == "..":
                if len(ans) >= 1:
                    ans.pop()
            elif char:
                ans.append(char)
        return ("/" + "/".join(ans))

                