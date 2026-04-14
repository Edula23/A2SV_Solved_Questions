class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        longest = -1
        res = set()
        def backTrack(curr, idx, lCount, rCount):
            nonlocal res, longest
            
            if idx >= len(s):
                if lCount == rCount:
                    if len(curr) > longest:
                        res = set()
                        res.add("".join(curr))
                        longest = len(curr)
                    elif len(curr) == longest:
                        res.add("".join(curr))
            else:
                c = s[idx]
                if c == "(":
                    curr.append(c)
                    backTrack(curr, idx+1, lCount+1, rCount)
                    curr.pop()
                    backTrack(curr, idx+1, lCount, rCount)
                elif c == ")":
                    backTrack(curr, idx+1, lCount, rCount)
                    if lCount > rCount:
                        curr.append(c)
                        backTrack(curr, idx+1, lCount, rCount+1)
                        curr.pop()
                else:
                    curr.append(c)
                    backTrack(curr, idx+1, lCount, rCount)
                    curr.pop()
        backTrack([], 0, 0, 0)
        return (list(res) if res else [""])