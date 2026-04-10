class Solution:
    def splitString(self, s: str) -> bool:
        def backTrack(idx, prev):
            if idx == len(s):
                return True
            for j in range(idx, len(s)):
                num = int(s[idx:j+1])
                if num + 1 == prev and backTrack(j+1, num):
                    return True
            return False

        for i in range(len(s) - 1):
            num = int(s[:i+1])
            if backTrack(i+1, num):
                return True
        return False